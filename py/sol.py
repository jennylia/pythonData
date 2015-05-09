#!/usr/bin/env python
import collections
from collections import Counter
cnt = Counter()
f = open ('test.txt', 'r');

for line in f:
    for word in line.split():
        cnt[word] += 1

print cnt
f.close


out = open('output.txt', 'w')

#for each element in the counter, we would like to see what they are
for x in cnt:
    out.write(x + " " + str(cnt[x]))
    out.write("\n")

out.close
