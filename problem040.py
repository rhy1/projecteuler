#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

# D1
n = 1
length = 1
result = 1
# D10
while length < 10:
	n += 1
	length += len(str(n))
result *= int(str(n)[len(str(n)) - (length - 9)])
# D100
while length < 100:
	n += 1
	length += len(str(n))
result *= int(str(n)[len(str(n)) - (length - 99)])
# D1000
while length < 1000:
	n += 1
	length += len(str(n))
result *= int(str(n)[len(str(n)) - (length - 999)])
# D10000
while length < 10000:
	n += 1
	length += len(str(n))
result *= int(str(n)[len(str(n)) - (length - 9999)])
# D100000
while length < 100000:
	n += 1
	length += len(str(n))
result *= int(str(n)[len(str(n)) - (length - 99999)])
# D1000000
while length < 1000000:
	n += 1
	length += len(str(n))
result *= int(str(n)[len(str(n)) - (length - 999999)])

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
