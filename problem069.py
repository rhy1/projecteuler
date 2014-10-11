#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, multiprocessing, euler

def Worker(_rangeLow, _rangeHigh, _step, _processResults):
	currentMax = 0
	for i in xrange(_rangeLow, _rangeHigh + 1, _step):
		tot = euler.Totient(i)
		if tot != 0:
			division = float(i) / tot
			if division > currentMax:
				currentMax = division
				currentMaxN = i
	_processResults.append((currentMax, currentMaxN))

if __name__ == "__main__":
	startTime = time.time()
	result = 0

	TARGET_NUMBER = 1500	# DEBUG, should be 1000000 here
	PROCESS_COUNT = 3
	manager = multiprocessing.Manager()
	processResults = manager.list([])
	processes = []

	for i in xrange(PROCESS_COUNT):	# using balanced workers here, they stop almost simultaneously
		processes.append(multiprocessing.Process(target = Worker, args = (i, TARGET_NUMBER, PROCESS_COUNT, processResults)))
		processes[i].start()
	for i in xrange(PROCESS_COUNT):
		processes[i].join()
	currentMax = 0
	print processResults	# DEBUG
	for i in xrange(len(processResults)):
		(m, n) = processResults[i]
		if m > currentMax:
			result = n
			currentMax = m

	print result
	finishTime = time.time()
	print "Execution time: ", finishTime - startTime

