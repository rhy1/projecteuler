#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler
from math import sqrt
from math import trunc

startTime = time.time()
result = 0

#------------------------------------------

def IsGoldbach(_n):
	prime = 2
	while prime < _n:
		a = sqrt((_n - prime) / 2)
		if a == trunc(a):
			#print _n, "=", prime, "+ 2 *", a, "** 2" # DEBUG
			return True
		prime = euler.NextPrime(prime)
	return False

n = 9
while IsGoldbach(n) or euler.IsPrime(n):
	n += 2
result = n
	
#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
