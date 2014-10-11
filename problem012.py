#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

i = 1
n = 1
while euler.CountDivisors(n) <= 500:
	i += 1
	n = i * (i + 1) / 2

result = n

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
