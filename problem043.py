#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

#n = 1023456789
#while n < 10000000000:
#	s = str(n)
#	if euler.IsPandigital09(s):
#		if (int(s[1] + s[2] + s[3]) % 2 == 0) and (int(s[2] + s[3] + s[4]) % 3 == 0) and (int(s[3] + s[4] + s[5]) % 5 == 0) and (int(s[4] + s[5] + s[6]) % 7 == 0) and (int(s[5] + s[6] + s[7]) % 11 == 0) and (int(s[6] + s[7] + s[8]) % 13 == 0) and (int(s[7] + s[8] + s[9]) % 17 == 0):
#			result += n
#	if n % 10000000 == 0: # DEBUG
#		print "progress: " + str(round((n - 1023456789) / (10000000000 - 1023456789) * 100, 5)) + "%, time passed: " + str(time.time() - startTime) + ", current n = " + str(n)
#	n += 1

triads = [[], [], [], [], [], [], [], [], [], []]
for i in xrange(0, 10, 2):
	for j in xrange(0, 10):
		for k in xrange(0, 10):
			if (i + j + k) % 3 == 0:
				triads[i].append((j, k))

for d0 in xrange(1, 10):				# 1 2 3 4 5 6 7 8 9
	for d3 in xrange(0, 10, 2):			# 0 2 4 6 8
		for (d2, d4) in triads[d3]:		# plenty of combinations here
			for d5 in xrange(0, 6, 5):	# 0 5
				for d1 in xrange(0, 10):
					low = 1000000000 * d0 + 100000000 * d1 + 10000000 * d2 + 1000000 * d3 + 100000 * d4 + 10000 * d5
					high = low + 10000
					n = low
					while n < high:
						s = str(n)
						if euler.IsPandigital09(s) and (int(s[4:7]) % 7 == 0) and (int(s[5:8]) % 11 == 0) and (int(s[6:9]) % 13 == 0) and (int(s[7:10]) % 17 == 0):
							result += n
						n += 1

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
