#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

i100 = 0
while i100 <= 2:
	i50 = 0
	while i50 <= 4:
		i20 = 0
		while i20 <= 10:
			i10 = 0
			while i10 <= 20:
				i5 = 0
				while i5 <= 40:
					i2 = 0
					while i2 <= 100:
						if i100 * 100 + i50 * 50 + i20 * 20 + i10 * 10 + i5 * 5 + i2 * 2 <= 200:
							result += 1
						i2 += 1
					i5 += 1
				i10 += 1
			i20 += 1
		i50 += 1
	i100 += 1
result += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
