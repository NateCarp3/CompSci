"""Author: Nathan Carpenter
Created on June 3, 2022"""
import math
class QuadraticEquation:

    def __init__(self, a, b, c):
        '''Constructor function that takes the input values and assigns
        them to an object using 'self' '''
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        '''If a is 0 throw an error, assign the input variables to self
            and make them a float'''
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    '''These functions return the objects value of a, b, and c'''
    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def discriminant(self):
        return self.getB()**2 - (4 * self.getA() * self.getC())

    def root1(self):
        det = self.discriminant()
        if det < 0:
            return None
        else:
            return (-self.getB() + math.sqrt(det))/(2*self.getA())

    def root2(self):
        det = self.discriminant()
        if det < 0:
            return None
        else:
            return (-self.getB() - math.sqrt(det))/(2*self.getA())

    def __str__(self):
        x = ""
        if self.getA() < 0:
            x += str('-')
        if abs(self.getA()) != 1:
            x += str(abs(self.getA()))
        x += str("x^2")
        if self.getB() != 0:
            if self.getB() < 0:
                x += ' - '
            else:
                x += " + "
            if abs(self.getB()) != 1:
                x += str(abs(self.getB()))
            x += 'x'
        if self.getC() < 0:
            x += ' - '
            x += str(abs(self.getC()))
        if self.getC() > 0:
            x += ' + '
            x += str(abs(self.getC()))
        x += " = 0"
        return x

