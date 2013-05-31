#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import binascii
import os
import sys

def hex2bin(string):
    return binascii.unhexlify(string)

def main(argv=None):
    if sys.argv is not None:
        argv = sys.argv

    for path in argv[1:]:
        with open(path, 'r') as fd:
            for line in fd:
                line = line.rstrip(os.linesep)
                line_bin = hex2bin(line)
                print base64.b16encode(line_bin)
                print base64.b64encode(line_bin)
    return 0

if __name__ == '__main__':
    sys.exit(main())
