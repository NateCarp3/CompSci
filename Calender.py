'''
Created on April 20, 2022
@author:   Nathan Carpenter
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
                self.day == d2.day
    def tomorrow(self):
        '''Increase the day by one. If it is the last day in the month, increase
            the month by one. If it is the last month of the year increase
            the year by one.'''
        if self.day == 28 and self.month == 2 and self.isLeapYear() == True:
            self.day +=1
        elif self.day >= DAYS_IN_MONTH[self.month]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        else:
            self.day += 1
        return self

    def yesterday(self):
        '''Decrease the day by one and update the month and year accordingly'''
        if self.day == 1 and self.month == 3 and self.isLeapYear() == True:
            self.month -= 1
            self.day = 29
        elif self.day <= 1:
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month]
            if self.month <1:
                self.month = 12
                self.day = DAYS_IN_MONTH[self.month]
                self.year -= 1
        else:
            self.day -= 1
        return self

    def addNDays(self, N):
        '''Add 'N' amount of days to the current date'''
        print(self)
        for day in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        print(self)
        for day in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        if self == d2:
            return False
        if self.year > d2.year:
            return False
        if self.month > d2.month and self.year >= d2.year:
            return False
        if self.year >= d2.year and self.month >= d2.month and self.day > d2.day:
            return False
        else:
            return True

    def isAfter(self, d2):
        if self == d2:
            return False
        if self.year < d2.year:
            return False
        if self.month < d2.month and self.year <= d2.year:
            return False
        if self.year <= d2.year and self.month <= d2.month and self.day < d2.day:
            return False
        else:
            return True

    def diff(self, d2):
        x = self.copy()
        y = d2.copy()
        if x == y:
            return 0
        z = 0
        while x.isBefore(y):
            x.tomorrow()
            z -= 1
        while x.isAfter(y):
            x.yesterday()
            z += 1
        return z-1
            
d = Date(11, 9, 2011)
d2 = Date(12,16,2011)
print(d2.diff(d))
#print("----------")
#print(d.diff(d2))
  
            
            

    
            
            
            
            
            
