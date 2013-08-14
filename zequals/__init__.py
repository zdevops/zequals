#
# Based on a Numberphile video :)
#

import math
from functools import wraps

def zequals(value):
	"""Returns the zequals value for any number, based on
	from what I get from the video is strict 'zequalling' :)
	For example : zequals(103) -> 100
				  zequals(26) -> 30	              
	It runs 'strict' zequalification (lol) so [-5,5] zequals
	to 0 :)
	"""
	try:
		float(value)
	except ValueError:
		raise ValueError('zequals : Fail! Not a number %s' % value)
	if value % 10:
		if value % 10 >= 5:
			value = value + (10 - value % 10)
		else:
			value = value - (value % 10)
	return value


def zAdd(a,b):
	"""Add two numbers
	"""
	return zequals(a) + zequals(b)

def zSub(a,b):
	"""Substract two numbers
	"""
	return zequals(a) - zequals(b)

def zMul(a,b):
	"""Multiply two numbers
	"""
	return zequals(a) * zequals(b)

def zDiv(a,b):
	"""Divide a by by
	"""
	return zequals(a) / zequals(b)


def z(x):
	"""Warning all arguments to wrapped function will be 'zequallified'
	still need to add the kwargs to this.....
	"""
	@wraps(x)
	def eek(*args, **kwargs):
		# TODO implement function scanning and zequalifying :)
		# For now : only do it on arguments :)
		newargs = []
		for arg in args:
			newargs.append(zequals(arg)) 
		return x(*newargs, **kwargs)
	return eek


