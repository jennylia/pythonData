#!/usr/bin/env python
print "hi"
import heapq
from heapq import heapify, heappush, heappop 
def heapsort(list):
    h = []
    for i in list:
        heappush(h,i)
    return [heappop(h) for i in range (len (h))]

x= [1,111,23232,423,345345,2,5,2,7,4]
x2 = [1,2,3,4,5,6,7]

#print heapsort(x)
  
print heapq.heapify(x)
print x
y = [heappop(x) for i in range (len (x))]
print y

print heapq._heapify_max(x2)
print x2
y2 = heapq.nlargest(1,x2)
#y2 = [heapq._heappop_max(x2) for i in range (len (x2))]
print y2
