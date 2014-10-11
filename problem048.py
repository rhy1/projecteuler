#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

psum = 0
for n in xrange(1, 1001):
	psum += n ** n
result = psum % 10000000000

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
