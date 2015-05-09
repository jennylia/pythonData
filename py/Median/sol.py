#!/usr/bin/env python
import collections
from collections import Counter

cnt = Counter()
f = open ('test.txt', 'r');

for line in f:
    print len(line.split())
f.close


#out = open('output.txt', 'w')

#for each element in the counter, we would like to see what they are
#x = "hello"
#y = "world"
#out.write(x)
#out.write("\n");
#out.write(y)

#out.close
