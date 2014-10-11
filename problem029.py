#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 100

combinations = []
a = 2
while a <= TARGET_NUMBER:
	b = 2
	while b <= TARGET_NUMBER:
		power = a ** b
		if not (power in combinations):
			combinations.append(power)
		b += 1
	a += 1
result = len(combinations)

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
