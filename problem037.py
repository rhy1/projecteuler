#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

def IsTruncatable(_n):
	s = str(_n)
	i = len(s) - 1
	while i > 0:
		if not euler.IsPrime(int(s[:-i])):
			return False
		i -= 1
	i = len(s) - 1
	while i > 0:
		if not euler.IsPrime(int(s[i:])):
			return False
		i -= 1
	if not euler.IsPrime(_n):
		return False
	return True

TARGET_NUMBER = 11
count = 0

n = 8
while count < TARGET_NUMBER:
	if IsTruncatable(n):
		result += n
		count += 1
		print "found", n # DEBUG
	n += 1
	if str(n)[0] == "1":
		n = int("2" + "0" * (len(str(n)) - 2) + "1")

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
