#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 1001

squareCt = 1 + (TARGET_NUMBER - 1) / 2
i = 2
while i <= squareCt:
	result += ((2 * i - 1) ** 2) * 4 - 6 * (2 * i - 1) + 6
	i += 1
result += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
