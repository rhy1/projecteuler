#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 10 ** 9
POWER = 5

i = 2
while i < TARGET_NUMBER:
	sum1 = 0
	for c in str(i):
		sum1 += int(c) ** POWER
	if sum1 == i:
		print i # DEBUG
		result += i
	i += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
