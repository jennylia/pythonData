#!/usr/bin/env python
"""
The important libraries to import
"""

import os
import numpy
import functools
import heapq
from heapq import heapify, heappush, heappop, _heapify_max,_siftup_max


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
heapq._heapify_max(leftHeap)

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
	print "***************Start Right Here******************"
	print "***n is: " + str(n)
	print "***curMedian is: " + str(curMedian)
	print "rightHeap length: " + str(len(rightHeap))
	print "leftHeap: " + str(len(leftHeap))
	print "rightHeap is: "
	print rightHeap
	print "leftHeap is: "
	print leftHeap

	print "Coding"
	if (len(rightHeap) > len(leftHeap)):
		print "===RIGHT LONGER==="
		print "n is: " + str(n)
		print "curMedian is: " + str(curMedian)
		if(n >= curMedian):
			heapq.heappush(leftHeap, -curMedian)

			tryMedian = rightHeap[0]
			if (tryMedian > n):
				curMedian = n
			else:
				curMedian = heapq.heappop(rightHeap)
				heapq.heappush(rightHeap, n) 

		else:
			heapq.heappush(leftHeap,-n)
	elif (len(leftHeap) > len(rightHeap)):
		print "===LEFT LONGER==="
		print "n is: " + str(n)
		print "curMedian is: " + str(curMedian)
		if(n <= curMedian):
			heapq.heappush(rightHeap, curMedian)
			print "$$$$$$$$$$$ Pay attention Left Heap"
			print leftHeap
			print "$$$$$$$$$$$ Pay attention Right Heap"
			print rightHeap
			#curMedian = -heapq.heappop(leftHeap)
			#what is the current Median is still smaller
			tryMedian = -leftHeap[0]
			if (tryMedian < n):
				curMedian = n
			else:
				curMedian = -heapq.heappop(leftHeap)
				heapq.heappush(leftHeap, -n)
			print "$$$$$$$$$$$ Pay attention CurMeidan"
			print curMedian
            #curMedian = left[0]
		else:
			heapq.heappush(rightHeap,n)

	else:
		print "===EQUAL || < 1 Diff LENGTH==="
		print "n is: " + str(n)
		print "curMedian is: " + str(curMedian)
		if (n > curMedian):
			heapq.heappush(rightHeap, n)
			print "$$$$$$$$$$$ Pay attention Left Heap"
			print leftHeap
			print "$$$$$$$$$$$ Pay attention Right Heap"
			print rightHeap
		else:
			heapq.heappush(leftHeap, -n)
			print "$$$$$$$$$$$ Pay attention Left Heap"
			print leftHeap
			print "$$$$$$$$$$$ Pay attention Right Heap"
			print rightHeap

	#TReturn the median:
	#This logic is more suited for added

	print "*****RETURNING MEDIAN*****"
	if (len(leftHeap) == len(rightHeap)):
		print "===EQUAL LENGTH==="
		print "Returned Median: " + str(curMedian)
		return curMedian
	elif (len(leftHeap) > len(rightHeap)):
		if(len(leftHeap)>0):
			print "@@leftHeap [0]"
			print leftHeap[0]
			print leftHeap
			heapq.heapify(leftHeap)
			print "@@leftHeap [0]"
			print leftHeap[0]
		print "===LEFT LONGER==="
		print "Returned Median: " + str(((-leftHeap[0] + curMedian)/2))
	
		return ((-leftHeap[0] + curMedian)/2)
	else:
		if(len(rightHeap)>0):
		#return (heapq.heappop(leftHeap) + curMedian)/2
			print "@@rightHeap [0]"
			print rightHeap[0]
		print "===RIGHT LONGER==="
		print "Returned Median: " + str(((rightHeap[0] + curMedian)/2))
		return ((rightHeap[0] + curMedian)/2)
		#return (heapq.heappop(rightHeap) + curMedian)/2
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
		num = float(line.rstrip('\n'))
		med = runningMed(num)
		outputFile.write(str(med) + '\n')

	inputFile.close()
	outputFile.close()
