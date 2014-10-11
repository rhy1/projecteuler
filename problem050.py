#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

primes = []
i = 2
while i < 1000000:
	primes.append(i)
	i = euler.NextPrime(i)

maxChainLen = 1
for i in xrange(0, len(primes)):
	psum = primes[i]
	for j in xrange(i + 1, len(primes)):
		psum += primes[j]
		if psum >= 1000000:
			break
		#if (j - i + 1) > maxChainLen and (psum in primes):
		if (j - i + 1) > maxChainLen and (euler.IsPrime(psum)):
			maxChainLen = j - i + 1
			result = psum
			print "Sum =", psum, " chain length =", maxChainLen

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
