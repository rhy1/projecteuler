#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler, datetime

startTime = time.time()
result = 0

#------------------------------------------

FIRST_DATE = datetime.date(1901, 1, 1)
LAST_DATE = datetime.date(2000, 12, 31)

dt = FIRST_DATE
while dt <= LAST_DATE:
	if (dt.day == 1) and (dt.isoweekday() == 7):
		result += 1
		print dt # DEBUG
	dt += datetime.timedelta(days = 1)

#------------------------------------------

print result
finishTime = time.time()
print "Execution time: ", finishTime - startTime
