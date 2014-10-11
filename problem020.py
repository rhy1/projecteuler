#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

mul = 1
i = 100
while i > 0:
	mul *= i
	i -= 1
i = len(str(mul)) - 1
while i >= 0:
	result += int(str(mul)[i])
	i -= 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
