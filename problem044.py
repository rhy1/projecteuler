#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler
from math import sqrt
from sys import maxint

startTime = time.time()
result = maxint

#------------------------------------------

def Check(_pa, _pb):
	pc = _pb + _pa
	c1 = (0.5 + sqrt(0.25 + 6 * pc)) / 3
	c2 = (0.5 - sqrt(0.25 + 6 * pc)) / 3
	if ((c1 < 0) or (c1 != int(c1))) and ((c2 < 0) or (c2 != int(c2))):
		return False
	pd = _pb - _pa
	d1 = (0.5 + sqrt(0.25 + 6 * pd)) / 3
	d2 = (0.5 - sqrt(0.25 + 6 * pd)) / 3
	if ((d1 < 0) or (d1 != int(d1))) and ((d2 < 0) or (d2 != int(d2))):
		return False
	return True


TARGET_NUMBER = 3000

a = 1
while (a < TARGET_NUMBER):
	pa = a * (3 * a - 1) / 2
	b = a + 1
	while (b < TARGET_NUMBER):
		pb = b * (3 * b - 1) / 2
		if (pb - pa < result) and (Check(pa, pb)):
			print a, b # DEBUG
			result = pb - pa
		b += 1
	a += 1

if result == maxint:
	result = 0

# def Pentagonal(n):
# 	return n * (3 * n - 1) / 2

# def SearchFunc(_low, _high):
# 	for i in first100000[_low:_high]:
# 		for j in first100000[:_high]:
# 			if (i > j) and ((i + j) in first100000) and ((i - j) in first100000):
# 				print i, j, i - j

# if __name__ == "__main__":
	# proc0 = multiprocessing.Process(target = SearchFunc, args = (0, 12500, ))
	# proc1 = multiprocessing.Process(target = SearchFunc, args = (12500, 25000, ))
	# proc2 = multiprocessing.Process(target = SearchFunc, args = (25000, 37500, ))
	# proc3 = multiprocessing.Process(target = SearchFunc, args = (37500, 50000, ))
	# proc4 = multiprocessing.Process(target = SearchFunc, args = (50000, 62500, ))
	# proc5 = multiprocessing.Process(target = SearchFunc, args = (62500, 75000, ))
	# proc6 = multiprocessing.Process(target = SearchFunc, args = (75000, 87500, ))
	# proc0.start()
	# proc1.start()
	# proc2.start()
	# proc3.start()
	# proc4.start()
	# proc5.start()
	# proc6.start()
	# proc0.join()
	# proc1.join()
	# proc2.join()
	# proc3.join()
	# proc4.join()
	# proc5.join()
	# proc6.join()

#------------------------------------------

	# print result
	# finishTime = time.time()
	# print "Execution time: ", finishTime - startTime

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
