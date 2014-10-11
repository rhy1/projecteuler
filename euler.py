#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt

def IsPrime(_n):
	if _n % 2 == 0:
		return False
	if _n > 841:
		if _n % 3 == 0:
			return False
		if _n % 5 == 0:
			return False
		if _n % 7 == 0:
			return False
		if _n % 11 == 0:
			return False
		if _n % 13 == 0:
			return False
		if _n % 17 == 0:
			return False
		if _n % 19 == 0:
			return False
		if _n % 23 == 0:
			return False
		if _n % 29 == 0:
			return False
		for i in xrange(31, int(sqrt(_n)), 2):
			if _n % i == 0:
				return False
	else:
		for i in xrange(3, int(sqrt(_n)) + 1, 2):
			if _n % i == 0:
				return False
	if _n < 2:
		return False
	return True

def NextPrime(_n):
	if _n % 2 == 1:
		i = _n + 2
	else:
		i = _n + 1
	while not IsPrime(i):
		i = i + 2
	return i

def CountDivisors(_n):
	# число натуральных делителей _n
	result = 0
	i = 1
	sqrt = _n ** 0.5
	while i < sqrt:
		if _n % i == 0:
			result += 2
		i += 1
	if (_n ** 0.5 == round(sqrt)) and (_n != 1):
		result += 1
	return result

def ListDivisors(_n):
	# натуральные делители _n, меньшие _n
	result = [1]
	i = 2
	sqrt = _n ** 0.5
	while i < sqrt:
		if _n % i == 0:
			result.append(i)
			result.append(_n / i)
		i += 1
	if (sqrt == round(sqrt)) and (_n != 1):
		result.append(sqrt)
	return result

def ListDivisorPairs(_n):
	# список кортежей (делитель1, делитель2), где перечислены все пары натуральных делителей числа,
	# причем делитель1 <= делитель2
	result = [(1, _n)]
	i = 2
	sqrt = _n ** 0.5
	while i < sqrt:
		if _n % i == 0:
			result.append((i, _n / i))
		i += 1
	if (sqrt == round(sqrt)) and (_n != 1):
		result.append((sqrt, sqrt))
	return result

def IsPalindrome(_s):
	for i in xrange(int(round(len(_s) / 2))):
		if _s[i] != _s[-(i + 1)]:
			return False
	return True

def IsPandigital19(_s):
	l = len(_s)
	if l > 9:
		return False
	elif l == 1:
		return _s == "1"
	elif l == 2:
		return ("1" in _s) and ("2" in _s)
	elif l == 3:
		return ("1" in _s) and ("2" in _s) and ("3" in _s)
	elif l == 4:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s)
	elif l == 5:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s)
	elif l == 6:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s)
	elif l == 7:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s)
	elif l == 8:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s) and ("8" in _s)
	elif l == 9:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s) and ("8" in _s) and ("9" in _s)
	else:
		return False

def IsPandigital09(_s):
	l = len(_s)
	if l > 10:
		return False
	elif l == 1:
		return _s == "1"
	elif l == 2:
		return ("1" in _s) and ("2" in _s)
	elif l == 3:
		return ("1" in _s) and ("2" in _s) and ("3" in _s)
	elif l == 4:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s)
	elif l == 5:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s)
	elif l == 6:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s)
	elif l == 7:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s)
	elif l == 8:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s) and ("8" in _s)
	elif l == 9:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s) and ("8" in _s) and ("9" in _s)
	elif l == 10:
		return ("1" in _s) and ("2" in _s) and ("3" in _s) and ("4" in _s) and ("5" in _s) and ("6" in _s) and ("7" in _s) and ("8" in _s) and ("9" in _s) and ("0" in _s)
	else:
		return False

def ArePermutations(_s1, _s2):
	# TRUE for "ABAC" and "CBAA"
	if len(_s1) != len(_s2):
		return False
	for i in xrange(0, len(_s1)):
		if _s1.count(_s1[i]) != _s2.count(_s1[i]):
			return False
	return True

def DigitSum(_n):
	result = 0
	s = str(_n)
	for i in xrange(len(s)):
		result += int(s[i])
	return result

def AreRelPrime(_a, _b):
	# checks if numbers are relatively prime
	aDivisors = []
	i = 2
	sqrt = _a ** 0.5
	while i < sqrt:
		if _a % i == 0:
			aDivisors.append(i)
		i += 1
	if (sqrt == round(sqrt)) and (_a != 1):
		aDivisors.append(sqrt)
	i = 2
	sqrt = _b ** 0.5
	while i < sqrt:
		if (_b % i == 0) and (i in aDivisors):
			return False
		i += 1
	if (sqrt == round(sqrt)) and (_b != 1) and (sqrt in aDivisors):
		return False
	return True

def Totient(_n):
	# Totient function is used to determine the number of numbers less than _n which are relatively prime to _n
	# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, Totient(9)=6.
	result = 0
	for i in xrange(1, _n):
		if AreRelPrime(i, _n):
			result += 1
	return result
