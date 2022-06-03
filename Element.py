'''
Nathan Carpenter
Created on February 8th 2022
I pledge my honor that I have abided by the Stevens Honor System
'''
def myLength(L):
        '''Takes input of an element L and then returns the length of this element.'''
        if L == []:
            return 0
        if L == '':
            return 0
        return 1 + myLength(L[1:])

def dot(L, K):
    '''Takes the input of two lists L and K and returns the dot product of the two lists'''
    if L == [] or K == []:
        return 0.0
    if L!=K:
        return L[0]*K[0] + dot(L[1:], K[1:])#"Lists are different lengths. Dot product cannot be equated."
    return L[0]*K[0] + dot(L[1:], K[1:])

def explode(S):
    '''Takes string S as input and returns a list of of the characters, each of which is a string of length 1, in a list''' 
    if S == '':
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    '''Takes input of element e and sequence L. Returns index in which e is first found in sequence L. If e is not found in L,
    return the length of L'''
    if L == []:
        return myLength(L)
    if L == '':
        return myLength(L)
    if e == L[0]:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    '''Takes in element e and a list L as input. Returns a list identical to L except all elements identical to e have been removed.'''
    if L == []:
        return []
    if e == L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):
    '''Takes input of first a function f that takes input of a single function and returns either True or False. The second input
    is a list L. The filter function returns a new list containing all elements of L in which the first inputed function
    returns True.'''
    if L == []:
        return []
    if f(L[0]) != True:
        return myFilter(f, L[1:])
    return [L[0]] + myFilter(f, L[1:])

def deepReverse(L):
    '''Takes input of a list where some of the elements may be lists themselves and returns the list with its elements in reverse order.
    If one of the elements of the list is a list, then the elements of the list within the list are also reversed and returned.'''
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1])
