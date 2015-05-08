#!/usr/bin/env python
import os
import numpy

def median(lst):
    return numpy.median (numpy.array(lst))

f = open('numbers.txt', 'r')

list = []
for line in f:
    list.append(int(line.rstrip('\n')))
print list
print median(list)
f.close()
