import functools
import heapq
from heapq import heapify, heappush, heappop 

"""
The following method overrdes the comparison tool, reversing the power of > and <
This was added to trick the heapq into behaving like a max heap
"""
@functools.total_ordering
class ReverseCompare(object):
    def __init__(self, obj):
        self.obj = obj
    def __eq__(self, other):
        return isinstance(other, ReverseCompare) and self.obj == other.obj
    def __le__(self, other):
        return isinstance(other, ReverseCompare) and self.obj >= other.obj
    def __str__(self):
        return str(self.obj)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.obj)

letters = [1,2,3,4,5]
heap = map(ReverseCompare, letters)
print heap
heapq.heapify(heap)
print heap
# print heapq.heappop(heap) # prints z
# print heapq.heappop(heap) # prints z
# print heapq.heappop(heap) # prints z
# print heapq.heappop(heap) # prints z
z = [heapq.heappop(heap) for i in range (len (heap))]


#This is for min heap
x= [1,111,23232,423,345345,2,5,2,7,4]
heapq.heapify(x)
print x
y = [heappop(x) for i in range (len (x))]
print y

