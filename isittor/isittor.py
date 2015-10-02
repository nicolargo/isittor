#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# IsItTor
#
# Copyright (C) 2015 Nicolargo <nicolas@nicolargo.com>
#
# MIT Licence

__appname__ = "IsItTor"
__version__ = "1.2"
__author__ = "Nicolas Hennion <nicolas@nicolargo.com>"
__licence__ = "MIT"
# Syntax
__doc__ = '''\
Usage: IsItTor [options] <IPaddress> ...

Check if the given <IPaddress> is a Tor exit node.

Options:
    -q: Quiet mode (Only return code. No bulshit)
    -h: Display help and exit
    -v: Display version and exit
    -V: Switch on debug mode (Verbose)
'''

# Import lib
import getopt
import sys
import os
import logging
import requests
import tempfile
import pickle

# Global variables
TORLIST_URL = "https://www.dan.me.uk/torlist/"
RESET_COLOR='\033[0m'
OK_COLOR='\033[0;32m'
NOK_COLOR='\033[0;31m'

# Functions
def printSyntax():
    """
    Display the syntax of the command line
    """
    print(__doc__)


def printVersion():
    """
    Display the current software version
    """
    print(__appname__ + " version " + __version__)


def main():
    """
    Main function
    """

    global _DEBUG_
    _DEBUG_ = False

    # Manage args
    try:
        opts, args = getopt.getopt(sys.argv[1:], "qhvV")
    except getopt.GetoptError as err:
        # Print help information and exit:
        print("Error: " + str(err))
        printSyntax()
        sys.exit(os.EX_USAGE)
    for opt, arg in opts:
        if opt in ("-h"):
            printVersion()
            printSyntax()
            sys.exit(os.EX_OK)
        elif opt in ("-v"):
            printVersion()
            sys.exit(os.EX_OK)
        elif opt in ("-V"):
            _DEBUG_ = True
            # Verbose mode is ON
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s %(levelname)s - %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S',
            )
        elif opt in ("-q"):
            # Quiet mode is ON
            logging.basicConfig(
                level=logging.ERROR,
                format='%(asctime)s %(levelname)s - %(message)s',
                datefmt='%d/%m/%Y %H:%M:%S',
            )
        # Add others options here...
        else:
            printSyntax()
            sys.exit(os.EX_USAGE)

    # By default verbose mode is OFF
    if not _DEBUG_:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S',
        )
    logging.debug("Running %s version %s" % (__appname__, __version__))
    logging.debug("Debug mode is ON")

    # Test args
    if args == []:
        logging.error("Syntax error. Give an IP address in argument.")
        printSyntax()
        sys.exit(os.EX_USAGE)

    # Main loop
    req = requests.get(TORLIST_URL)
    tl = req.text.split('\n')
    tl_path = os.path.join(tempfile.gettempdir(), 'isittor.torlist')
    if len(tl) > 100:
        # List has been downloaded
        # Save it
        logging.info("Load TOR exit node list from %s" % TORLIST_URL)
        with open(tl_path, 'wb') as f:
            pickle.dump(tl, f)
    else:
        # List has not been downloaded (the site only return it every 30 mins)
        # Load it
        logging.info("Load TOR exit node list from %s" % tl_path)
        try:
            with open(tl_path, 'rb') as f:
                tl = pickle.load(f)
        except IOError as e:
            logging.critical("Can not load TOR exit node list from %s (%s)" % (tl_path, e))
            sys.exit(os.EX_DATAERR)

    ret = os.EX_OK
    for ip in args:
        if ip not in tl:
            logging.info("%s%s is NOT a TOR exit node%s" % (NOK_COLOR, ip, RESET_COLOR))
            ret = os.EX_SOFTWARE
        else:
            logging.info("%s%s is a TOR exit node%s" % (OK_COLOR, ip, RESET_COLOR))

    return ret

# Main
#=====

if __name__ == "__main__":
    main()

# The end...
