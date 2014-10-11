#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 10000

def IsUnusual(_n):
	divisors = euler.ListDivisorPairs(_n)
	for (a, b) in divisors:
		s = str(a) + str(b) + str(_n)
		if (len(s) == 9) and ("1" in s) and ("2" in s) and ("3" in s) and ("4" in s) and ("5" in s) and ("6" in s) and ("7" in s) and ("8" in s) and ("9" in s):
			return True
	return False

i = 1
while i < TARGET_NUMBER:
	if IsUnusual(i):
		result += i
	i += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
