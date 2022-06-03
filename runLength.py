"""Author: Nathan Carpenter
Created on March 23, 2022
I pledge my honor that I have abided by the Stevens Honor System
"""
########
# Step 1
# Complete the following definition.
# The helper lORL should be tail recursive, and use the accumulator technique.
########
import math

def listOfRunLength(s):
    "Assume s is a nonempty string. Return a list of the lengths of its runs.For the list L0 above, listOfRunLengths(L0) is [3,3,4,2,1,1,1]."""
    if len(s) == 1:
        result = [1]
        return result

    def lORL(s, result, curCount, curVal):
        """Accumulate, in result, the list of run lengths of s, using curCount as count of the current run; the current run is a sequence of curVals."""
        if s=="":
            result = []
            return result
        elif s[0] == curVal:
            curCount = count_bit(s, curVal)
            result += [curCount]
            return lORL(s[1:], result, curCOunt, curVal)
        else:
            return result
    return lORL(s[1:], [], 1, s[0] ) # don't change this line
    # first run has length 1 and begins with s[0]

########
# Step 2
# Complete the following definition.
########
def findRunBits(s):
    '''Returns the number of bits to use for compressing string s.
        Assume s is a nonempty string.
        Specifically, returns n where n is the log of the average
        run length, but at most 7, as described at the beginning of this file.
        The maximum n is 7 because only three bits are available
        for it (the bbb in the compressed format).'''
    avgLen = (sum(listOfRunLengths(s)))/len(listOfRunLengths(s))
    n = math.ceil(math.log(avgLen,2)) + 1
    runBits = min(n,7)
    return runBits
#This solution utilizes the built in functions: sum, min, len, log and ceiling. No recursion is used.



    
    
