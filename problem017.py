#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

startTime = time.time()
result = 0

#------------------------------------------

for n in xrange(10001, 11001):
	s = str(n)
	# 10 ** 3
	if s[1] == "0":
		ct = 0
	else:
		# one thousand
		ct = 11
	# 10 ** 2
	if s[2] == "1":
		# one hundred
		ct += 10
	elif s[2] == "2":
		# two hundred
		ct += 10
	elif s[2] == "3":
		# three hundred
		ct += 12
	elif s[2] == "4":
		# four hundred
		ct += 11
	elif s[2] == "5":
		# five hundred
		ct += 11
	elif s[2] == "6":
		# six hundred
		ct += 10
	elif s[2] == "7":
		# seven hundred
		ct += 12
	elif s[2] == "8":
		# eight hundred
		ct += 12
	else:
		# nine hundred
		ct += 11
	# and
	if (ct != 0) and (s[3:] != "00"):
		ct += 3
	# 10 ** 1
	if s[3] == "1":
		if s[4] == "0":
			# ten
			ct += 3
		elif s[4] == "1":
			# eleven
			ct += 6
		elif s[4] == "2":
			# twelve
			ct += 6
		elif s[4] == "3":
			# thirteen
			ct += 8
		elif s[4] == "4":
			# fourteen
			ct += 8
		elif s[4] == "5":
			# fifteen
			ct += 7
		elif s[4] == "6":
			# sixteen
			ct += 7
		elif s[4] == "7":
			# seventeen
			ct += 9
		elif s[4] == "8":
			# eighteen
			ct += 8
		else:
			# nineteen
			ct += 8
	else:
		if s[3] == "2":
			# twenty
			ct += 6
		elif s[3] == "3":
			# thirty
			ct += 6
		elif s[3] == "4":
			# forty
			ct += 5
		elif s[3] == "5":
			# fifty
			ct += 5
		elif s[3] == "6":
			# sixty
			ct += 5
		elif s[3] == "7":
			# seventy
			ct += 7
		elif s[3] == "8":
			# eighty
			ct += 6
		elif s[3] == "9":
			# ninety
			ct += 6
		if s[4] == "1":
			# one
			ct += 3
		elif s[4] == "2":
			# two
			ct += 3
		elif s[4] == "3":
			# three
			ct += 5
		elif s[4] == "4":
			# four
			ct += 4
		elif s[4] == "5":
			# five
			ct += 4
		elif s[4] == "6":
			# six
			ct += 3
		elif s[4] == "7":
			# seven
			ct += 5
		elif s[4] == "8":
			# eight
			ct += 5
		elif s[4] == "9":
			# nine
			ct += 4
	result += ct
	
#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
