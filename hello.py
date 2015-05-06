#!/usr/bin/env python

print "Hi there"

f = open('test.txt','r')

for line in f:
    print line,
f.close()
