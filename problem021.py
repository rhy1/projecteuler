#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

def IsAmicable(_n):
	divisors = euler.ListDivisors(_n)
	sum1 = 0
	sum2 = 0
	for divisor in divisors:
		sum1 += divisor
	divisors = euler.ListDivisors(sum1)
	for divisor in divisors:
		sum2 += divisor
	return ((_n == sum2) and (_n != sum1))

i = 1
while i < 10000:
	if IsAmicable(i):
		result += i
	i += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
