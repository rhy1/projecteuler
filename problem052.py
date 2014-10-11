#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

n = 1
while (not euler.ArePermutations(str(n), str(2 * n))) or (not euler.ArePermutations(str(n), str(3 * n))) or (not euler.ArePermutations(str(n), str(4 * n))) or (not euler.ArePermutations(str(n), str(5 * n))) or (not euler.ArePermutations(str(n), str(6 * n))):
	n += 1
result = n

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
