#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

def IsPandigital(_s):
	return (len(_s) == 9) and ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s) and ("8" in _s) and ("9" in _s)

for n in xrange(1, 99999):
	for b in xrange(2, 10):
		s = ""
		for i in xrange(1, b + 1):
			s += str(n * i)
		if (int(s) > result) and (IsPandigital(s)):
			result = int(s)

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
