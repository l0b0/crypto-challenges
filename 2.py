#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def xor(operands):
    result = operands[0]
    for operand in operands[1:]:
        result = result ^ operand
    return result

def main(argv=None):
    if sys.argv is not None:
        argv = sys.argv

    lines_bin = []
    for path in argv[1:]:
        with open(path, 'r') as fd:
            for line in fd:
                line = line.rstrip(os.linesep)
                lines_bin.append(int(line, 16))
    result = xor(lines_bin)
    print hex(result)[2:].rstrip("L")
    return 0

if __name__ == '__main__':
    sys.exit(main())
