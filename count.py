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
