#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

startTime = time.time()

result = 0

for i in range(1000):
	if (i % 3 == 0) or (i % 5 == 0):
		result = result + i

print result

finishTime = time.time()
print "Execution time: ", finishTime - startTime
