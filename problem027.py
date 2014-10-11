#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 1000

maxa = 0
maxb = 0
maxct = 0

a = -TARGET_NUMBER + 1
while a < TARGET_NUMBER:
	b = -TARGET_NUMBER + 1
	while b < TARGET_NUMBER:
		n = 0
		while euler.IsPrime(n ** 2 + a * n + b):
			n += 1
		if n > maxct:
			maxct = n
			maxa = a
			maxb = b
		b += 1
	a += 1
result = maxa * maxb

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
