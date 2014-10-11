#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

startTime = time.time()
result = 0

#------------------------------------------

n1 = 1
n2 = 1
while n2 < 4000000:
	if n2 % 2 == 0:
		result = result + n2
	n3 = n1 + n2
	n1 = n2
	n2 = n3

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
