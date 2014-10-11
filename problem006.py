#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

startTime = time.time()
result = 0

#------------------------------------------

s1 = 0
s2 = 0
i = 1
while i < 101:
	s1 += i ** 2
	s2 += i
	i += 1
s2 = s2 ** 2
result = s2 - s1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
