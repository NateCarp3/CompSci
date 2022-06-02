Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##################################################################
>>> #Nathan Carpenter
>>> #I pledge my honor that I have abided by the Stevens Honor Code
>>> # CS 115A Lab 1
>>> #######################################################################
>>> from math import factorial
>>> 
>>> def inverse(n):
	return 1/n

>>> def e(n):
	mylist = list(range(1, n+1))
	return 1+sum(map(inverse, map(factorial, mylist)))

>>> e(2)
2.5
>>> 
