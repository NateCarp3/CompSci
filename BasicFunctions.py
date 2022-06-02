#Nathan Carpenter
#I pledge my honor that I have abided by the Stevens Honor System
from functools import reduce
def mult(x,y):
    """Returns the product of x and y"""
    return x * y
def factorial(n):
    """Takes positive integer n and returns n!"""
    return reduce(mult, range(1,n+1))
def add(x,y):
    """Returns the sum of x and y"""
    return x+y
def mean(L):
    """takes a list and returns the average"""
    return reduce(add, L)/ len(L)
