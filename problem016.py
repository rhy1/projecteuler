#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

s = str(2 ** 1000)
i = 0
while i < len(s):
	result += int(s[i])
	i += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
