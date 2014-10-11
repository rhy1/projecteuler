#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

TARGET_NUMBER = 362880 * 7

def IsCurious(_n):
	global fac
	facsum = 0
	s = str(_n)
	for i in xrange(0, len(s)):
		facsum += fac[int(s[i])]
	return facsum == _n

for i in xrange(3, TARGET_NUMBER):
	if IsCurious(i):
		result += i
		print i # DEBUG

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
