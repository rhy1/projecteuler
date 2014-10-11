#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 10001

i, n = 1, 2
while i < TARGET_NUMBER:
	n = euler.NextPrime(n)
	i = i + 1
result = n

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
