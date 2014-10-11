#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

result = 1
s = list("0000000000000000000011111111111111111111")
while s != list("1111111111111111111100000000000000000000"):
	i = 39
	while (i > 0) and ((s[i] == "0") or (s[i - 1] == "1")):
		i -= 1
	if (i > 1) or ((i == 1) and (s[i - 1] == "0")):
		s[i - 1] = "1"
		s[i] = "0"
		ct = ("".join(s[i + 1:])).count("1")
		s = list("".join(s[:i + 1]) + "0" * (len(s[i + 1:]) - ct) + "1" * ct)
	result += 1
	if result % 1000000 == 0:					# DEBUG
		progress = 100 * (int("0b" + "".join(s), 2) - int("0b0000000000000000000011111111111111111111", 2)) / (int("0b1111111111111111111100000000000000000000", 2) - int("0b0000000000000000000011111111111111111111", 2))
		print "".join(s), "(" + str(round(progress, 5)) + "%), time passed:", str(round(time.time() - startTime))

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
