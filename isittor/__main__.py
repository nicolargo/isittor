#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# IsItTor
#
# Copyright (C) 2015 Nicolargo <nicolas@nicolargo.com>
#
# MIT Licence

# Execute with:
# $ python isittor/__main__.py (2.6)
# $ python -m isittor          (2.7+)

import sys

if __package__ is None and not hasattr(sys, "frozen"):
    # It is a direct call to __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(path)))

import isittor

if __name__ == '__main__':
    isittor.main()
