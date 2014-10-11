#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from euler import IsPrime
from math import log10

if __name__ == "__main__":
	startTime = time.time()
	result = 0

#------------------------------------------

	MAX_N = 10000

	catl = lambda _n1, _n2: _n1 * (10 ** int(1 + log10(_n2))) + _n2
	checkl = lambda _n1, _n2: (IsPrime(catl(_n1, _n2)) and IsPrime(catl(_n2, _n1)))

	for n0 in xrange(3, MAX_N, 2):
		if IsPrime(n0):
			for n1 in xrange(n0 + 2, MAX_N, 2):
				if IsPrime(n1) and checkl(n1, n0):
					for n2 in xrange(n1 + 2, MAX_N, 2):
						if IsPrime(n2) and checkl(n2, n0) and checkl(n2, n1):
							for n3 in xrange(n2 + 2, MAX_N, 2):
								if IsPrime(n3) and checkl(n3, n0) and checkl(n3, n1) and checkl(n3, n2):
									for n4 in xrange(n3 + 2, MAX_N, 2):
										if IsPrime(n4) and checkl(n4, n0) and checkl(n4, n1) and checkl(n4, n2) and checkl(n4, n3):
											break
									else:
										continue
									break
							else:
								continue
							break
					else:
						continue
					break
			else:
				continue
			break

	if n0 < MAX_N - 1:
		print n0, n1, n2, n3, n4 # DEBUG
		result = n0 + n1 + n2 + n3 + n4
	else:
		print "MAX_N reached"

#------------------------------------------

	print result
	finishTime = time.time()
	print "Execution time: ", finishTime - startTime
