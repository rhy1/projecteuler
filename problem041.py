#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

for n in xrange(1001, 10000):
	if euler.IsPandigital19(str(n)) and euler.IsPrime(n):
		result = n
for n in xrange(1000001, 10000000):
	if euler.IsPandigital19(str(n)) and euler.IsPrime(n):
		result = n

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
