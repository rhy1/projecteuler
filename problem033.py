#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

TARGET_NUMBER = 100

def Simplify(_a, _b):
	sb = str(_b)
	if sb[1] != "0":
		sa = str(_a)
		if (sa[0] == sb[0]) and (int(sa[1]) < int(sb[1])):
			return (1.0 * int(sa[1]) / int(sb[1]))
		if (sa[0] == sb[1]) and (int(sa[1]) < int(sb[0])):
			return (1.0 * int(sa[1]) / int(sb[0]))
		if (sa[1] == sb[0]) and (int(sa[0]) < int(sb[1])):
			return (1.0 * int(sa[0]) / int(sb[1]))
		if (sa[1] == sb[1]) and (int(sa[0]) < int(sb[0])):
			return (1.0 * int(sa[0]) / int(sb[0]))
	return 0

simples = []
for a in range(1, 9):
	for b in range(a + 1, 10):
		simples.append(1.0 * a / b)
for a in range(11, TARGET_NUMBER - 1):
	for b in range(a + 1, TARGET_NUMBER):
		smp = Simplify(a, b)
		if (smp == 1.0 * a / b) and (simples.count(smp) > 0):
			print a, b, smp # DEBUG	

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
