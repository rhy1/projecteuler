#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

DIGITS10 = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
DIGITS9 = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]

def FindLeastOfFamily(_n, _targetFamilySize):
	s = str(_n)
	maskLen = len(s)
	for wildCt in xrange(1, maskLen):
		# calculate first and last masks
		mask = s[:-wildCt - 1] + "*" * wildCt + s[-1]
		lastMask = "*" * wildCt + s[wildCt:]
		while True:
			familySize = 0
			if mask[0] != "*":
				for digit in DIGITS10:
					if euler.IsPrime(int(mask.replace("*", digit))):
						familySize += 1
						leastOne = int(mask.replace("*", digit))
			else:
				for digit in DIGITS9:
					if euler.IsPrime(int(mask.replace("*", digit))):
						familySize += 1
						leastOne = int(mask.replace("*", digit))
			if familySize == _targetFamilySize:
				return leastOne
			if mask == lastMask:
				break
			# calculate new mask
			i = maskLen - 1
			while (i > 0) and ((mask[i] != "*") or (mask[i - 1] == "*")):
				i -= 1
			if (i > 1) or ((i == 1) and (mask[i - 1] != "*")):
				if i != maskLen - 1:
					ct = mask[i + 1:].count("*")
				else:
					ct = 0
				mask = mask[:i - 1] + "*" + s[i:maskLen - ct] + "*" * ct
				#print "---", i, ct, mask, mask[:i - 1] # DEBUG
	return None

n = 2
while True:
	result = FindLeastOfFamily(n, 8)
	if result != None:
		break
	n = euler.NextPrime(n)

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
