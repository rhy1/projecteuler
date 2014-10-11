#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

startTime = time.time()
result = 0

#------------------------------------------

def IsPalindrome(n):
	s = str(n)
	for i in range(int(round(len(s) / 2))):
		if s[i] != s[-(i + 1)]:
			return False
	return True

n1 = 100
while n1 < 1000:
	n2 = 100
	while n2 < 1000:
		mul = n1 * n2
		if IsPalindrome(mul):
			if mul > result:
				result = mul
		n2 = n2 + 1
	n1 = n1 + 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
