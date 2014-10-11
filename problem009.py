#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 1000

c = TARGET_NUMBER
keepLooping = True
while (c > 0) and (keepLooping):
	c -= 1
	b = c
	while (b > 0) and (keepLooping):
		b -= 1
		a = b
		while (a > 0) and (keepLooping):
			a -= 1
			if (a + b + c == 1000) and (a ** 2 + b ** 2 == c ** 2):
				keepLooping = False
				break
result = a * b * c

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
