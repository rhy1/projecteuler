#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 2000000

n = 2
while n < TARGET_NUMBER:
	result += n
	n = euler.NextPrime(n)

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
