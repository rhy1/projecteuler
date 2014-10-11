#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 1000

i = 2
n1 = 1
n2 = 1
while len(str(n2)) < TARGET_NUMBER:
	(n1, n2) = (n2, n1 + n2)
	i += 1
result = i

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
