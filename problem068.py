#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, euler

if __name__ == "__main__":
	startTime = time.time()
	result = 0

#------------------------------------------

	for a0 in xrange(1, 10):
		for a1 in xrange(1, 10):
			if a1 != a0:
				for a2 in xrange(1, 10):
					if a2 != a1 and a2 != a0:
						for a3 in xrange(1, 10):
							if a3 != a2 and a3 != a1 and a3 != a0:
								for a4 in xrange(1, 10):
									if a4 != a3 and a4 != a2 and a4 != a1 and a4 != a0:
										for a5 in xrange(1, 11):
											if a5 != a4 and a5 != a3 and a5 != a2 and a5 != a1 and a5 != a0:
												for a6 in xrange(1, 11):
													if a6 != a5 and a6 != a4 and a6 != a3 and a6 != a2 and a6 != a1 and a6 != a0:
														for a7 in xrange(1, 11):
															if a7 != a6 and a7 != a5 and a7 != a4 and a7 != a3 and a7 != a2 and a7 != a1 and a7 != a0:
																for a8 in xrange(1, 11):
																	if a8 != a7 and a8 != a6 and a8 != a5 and a8 != a4 and a8 != a3 and a8 != a2 and a8 != a1 and a8 != a0:
																		for a9 in xrange(1, 11):
																			if a9 != a8 and a9 != a7 and a9 != a6 and a9 != a5 and a9 != a4 and a9 != a3 and a9 != a2 and a9 != a1 and a9 != a0:
																				line = a0 + a1 + a6
																				if a1 + a2 + a7 == line and a2 + a3 + a8 == line and a3 + a4 + a9 == line and a4 + a0 + a5 == line:
																					if a5 == min(a5, a6, a7, a8, a9) and \
																						int(str(a5) + str(a0) + str(a4) + str(a9) + str(a4) + str(a3) \
																						+ str(a8) + str(a3) + str(a2) + str(a7) + str(a2) + str(a1) \
																						+ str(a6) + str(a1) + str(a0)) > result \
																						and len(str(a5) + str(a0) + str(a4) + str(a9) + str(a4) + str(a3) \
																						+ str(a8) + str(a3) + str(a2) + str(a7) + str(a2) + str(a1) \
																						+ str(a6) + str(a1) + str(a0)) == 16:
																						result = int(str(a5) + str(a0) + str(a4) + str(a9) + str(a4) + str(a3) \
																							+ str(a8) + str(a3) + str(a2) + str(a7) + str(a2) + str(a1) \
																							+ str(a6) + str(a1) + str(a0))


#------------------------------------------

	print result
	finishTime = time.time()
	print "Execution time: ", finishTime - startTime
