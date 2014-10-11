#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 28123

abundant = []
i = 1
while i <= TARGET_NUMBER:
	divisors = euler.ListDivisors(i)
	sum1 = 0
	for divisor in divisors:
		sum1 += divisor
	if sum1 > i:
		abundant.append(i)

	foundOne = True
	j = 0
	while (j < len(abundant)) and foundOne:
		k = len(abundant) - 1
		while (k >= j) and foundOne:
			if abundant[j] + abundant[k] == i:
				foundOne = False
			k -= 1
		j += 1
	if foundOne:
		result += i
	i += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
