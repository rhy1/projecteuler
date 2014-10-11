#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 1000000

i = 1
while i < TARGET_NUMBER:
	if euler.IsPalindrome(str(i)) and euler.IsPalindrome(str(bin(i))[2:]):
		result += i
	i += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
