#! /usr/bin/env python

import os
import sys

infilename = sys.argv[1]
outfilename = '.'.join(infilename.split('.')[:-1]) + '.js'

ip = open(infilename,'r')
op = open(outfilename,'w')

for line in ip:
    if line.strip() == '': continue
    print >>op, """document.write('%s');""" % line.rstrip()

ip.close()
op.close()
