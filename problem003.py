#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 600851475143
halfRange = round(TARGET_NUMBER / 2) + 1
n = 2
while n <= halfRange:
	if TARGET_NUMBER % n == 0:
		result = n
		if euler.IsPrime(TARGET_NUMBER / n) and (TARGET_NUMBER / n > n):
			result = TARGET_NUMBER / n
			break
		print n # DEBUG
	n = euler.NextPrime(n)

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
