#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler
from math import factorial

startTime = time.time()
result = 0

#------------------------------------------

for n in xrange(1, 101):
	for r in xrange(1, n + 1):
		if factorial(n) / (factorial(r) * factorial(n - r)) > 1000000:
			result += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
