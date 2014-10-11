#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

def CountCollatzSteps(n):
	result = 1
	while n != 1:
		result += 1
		if n % 2 == 0:
			n = n / 2
		else:
			n = 3 * n + 1
	return result

UPPER_BORDER = 1000000
longestChain = 0
longestChainSeed = 0
i = 1
while i < UPPER_BORDER:
	chainLength = CountCollatzSteps(i)
	if chainLength > longestChain:
		longestChain = chainLength
		longestChainSeed = i
	i += 1
result = longestChainSeed

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
