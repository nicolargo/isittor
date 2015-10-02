# IsItTor

IsItTor is a script to check if an IP address is a Tor exit node.

Install:

   # sudo pip install requests[security] isittor

Usage:

    # isittor.py 99.245.160.4
    02/10/2015 14:22:00 INFO - Starting new HTTPS connection (1): www.dan.me.uk
    02/10/2015 14:22:01 INFO - Load TOR exit node list from https://www.dan.me.uk/torlist/
    02/10/2015 14:22:01 INFO - 99.245.160.4 is a TOR exit node


    # isittor.py 99.245.160.4 10.10.10.10
    02/10/2015 14:22:00 INFO - Starting new HTTPS connection (1): www.dan.me.uk
    02/10/2015 14:22:01 INFO - Load TOR exit node list from https://www.dan.me.uk/torlist/
    02/10/2015 14:22:01 INFO - 99.245.160.4 is a TOR exit node
    02/10/2015 14:22:01 INFO - 10.10.10.10 is NOT a TOR exit node
