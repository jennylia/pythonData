"""
The important libraries to import
"""

import os
import numpy
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





"""
runningMed(n)

Running Median
Signature: integer => integer
Purpose: To take an integer, and return the running median of all integers seen so far
Stub: 
	runningMed(4) => 4
	runningMed(5) => 4.5
	runningMed(4) => 4

Algorithm:
	1. The invariant: current median is always the current median
		leftHeap is a maxheap, always smaller than median
		rightHeap is a minheap, always bigger than median
		size of leftHeap and rightHeap shall not differ more than one
	2. If the size of both heap are equal, return curMedian
		else return the heappop of the heap with more element
	3. If one heap's size grows bigger than the other by more than one, balance:
		ex. rightHeap about to grow to be >2 than leftHeap
		heappush the median to the left heap
		median is now the heappop of the right heap
		add the item to the right

		For left just repeat

"""

#Set up
#Todo, move this above the comments
curMedian = 0
leftHeap = map(ReverseCompare, [])
rightHeap = []
heapq.heapify(rightHeap)
heapq.heapify(leftHeap)

def runningMed(n):
	#importing the global variables
	global curMedian 
	global leftHeap
	global rightHeap
	#The first time
	if (curMedian == 0):
		curMedian = n
		return curMedian

	#the second +... time
	# print "debug"
	# print rightHeap
	# print leftHeap
	# heapq.heappush(leftHeap, 3)
	# heapq.heappush(rightHeap, 3)
	# print rightHeap

	print "length of heaps"
	print len(rightHeap)
	print len(leftHeap)

	if (len(rightHeap) > len(leftHeap) + 2):
		print "Debug long right heap"

		if(n >= curMedian):
			heapq.heappush(leftHeap, curMedian)
			curMedian = heapq.heappop(rightHeap)
			heappop.heappush(rightHeap, n)
		else:
			heapq.heappush(leftHeap, n)

	elif (len(leftHeap) > len(rightHeap) + 2):
		print "Debug long"
		if(n <= curMedian):
			heapq.heappush(rightHeap, curMedian)
			curMedian = heapq.heappop(leftHeap)
			heappop.heappush(leftHeap, n)
		else:
			heapq.heappush(rightHeap,n)

	else:
		print "Debug curMedian"
		print n
		print curMedian
		if (n > curMedian):
			heapq.heappush(rightHeap, n)
		else:
			heapq.heappush(leftHeap,n)

	#TReturn the median:
	#This logic is more suited for added
	if (len(leftHeap) == len(rightHeap)):
		return curMedian
	elif (len(leftHeap) > len(rightHeap)):
		return (heapq.heappop(leftHeap) + curMedian)/2
	else:
		return (heapq.heappop(rightHeap) + curMedian)/2
	# the real one be like, if eqal length return med
	#else return average of media and the longer one




"""
The Main Class:

Summary:
To open the input and output file
"""

if __name__ == "__main__":
	#TODO: Input/output names must be changed
	inputFile = open('numbers.txt', 'r')
	outputFile = open('output.txt', 'w')

	for line in inputFile:
		num = int(line.rstrip('\n'))
		med = runningMed(num)
		outputFile.write(str(med) + '\n')

	inputFile.close()
	outputFile.close()