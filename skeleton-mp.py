#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, multiprocessing, euler

def Worker(_rangeLow, _rangeHigh, _processResults):
	# TODO

if __name__ == "__main__":
	startTime = time.time()
	result = 0

	TARGET_NUMBER = 1000000
	PROCESS_COUNT = 7
	manager = multiprocessing.Manager()
	processResults = manager.list([])
	processes = []
	rangeHigh = 0
	for i in xrange(PROCESS_COUNT):
		if i != PROCESS_COUNT - 1:
			rangeLow = rangeHigh + 1
			rangeHigh = rangeLow + int(TARGET_NUMBER / PROCESS_COUNT)
		else:
			rangeLow = rangeHigh + 1
			rangeHigh = TARGET_NUMBER
		processes.append(multiprocessing.Process(target = Worker, args = (rangeLow, rangeHigh, processResults)))
		processes[i].start()
	for i in xrange(PROCESS_COUNT):
		processes[i].join()

	# TODO: post-process processResults here

	print result
	finishTime = time.time()
	print "Execution time: ", finishTime - startTime

