#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

MIN_N = 1001
MAX_N = 9999

n1 = MIN_N
keepLooping = True
while keepLooping:
	while (n1 <= MAX_N) and (not euler.IsPrime(n1)):
		n1 += 2
	for step in xrange(2, (MAX_N - n1) / 2 + 1, 2):
		n2 = n1 + step
		if (euler.IsPrime(n2)) and (euler.ArePermutations(str(n1), str(n2))):
			n3 = n2 + step
			if (euler.IsPrime(n3)) and (euler.ArePermutations(str(n1), str(n3))) and ((n1, n2, n3) != (1487, 4817, 8147)):
				result = int(str(n1) + str(n2) + str(n3))
				keepLooping = False
				break
	n1 += 2

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
