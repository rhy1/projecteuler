#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

maxct = 0
for p in xrange(12, 1001):
	ct = 0
	for a in xrange(1, p / 4 + 1):
		for b in xrange(1, p - a):
			if a ** 2 + b ** 2 == (p - a - b) ** 2:
				print a, b, (p - a - b) # DEBUG
				ct += 1
	if ct > maxct:
		maxct = ct
		result = p

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
