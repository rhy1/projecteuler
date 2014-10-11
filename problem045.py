#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

t = 286
p = 166
h = 144

while (t * (t + 1) != p * (3 * p  - 1)) or (t * (t + 1) / 2 != h * (2 * h - 1)):
	if t * (t + 1) > p * (3 * p  - 1):
		p += 1
		continue
	if t * (t + 1) / 2 > h * (2 * h - 1):
		h += 1
		continue
	t += 1

result = t * (t + 1) / 2
	
#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
