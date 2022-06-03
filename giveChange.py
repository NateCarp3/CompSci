'''
Created on February 16th 2022
@author:   Nathan Carpenter

'''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    """ Takes the same kind of input as change. Then returns a list where the first item is the minimum number of coins needed"""
    if amount == 0:
        return [0, []]
    if coins ==[]:
        return [0, []]
    if coins[0] >  amount:
        return giveChange(amount, coins [1:])
    if coins
    use_it = giveChange(amount - coins[0])
    lose_it = giveChange(amount, coins[1:])
    
    if use_it[0] < lose_it[0]:
        return use_it
    return lose_it

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scrabbleScores):
        """returns the integer value of any letter in the game"""
        if scrabbleScores == []:
            return 0
        if scrabbleScores[0][0] == letter:
            return scrabbleScores[0][1]
        return letterScore(letter, scrabbleScroes[1:])
    def wordScore(s, scrabbleScores):
        """returns the scrabble value of a word"""
        if s == "":
            return []
        return [letterScore(s[0], scrabbleScores)] + wordScore_helper(s[1:], scrabbleScores)

    if dct == []:
        return []
    return [[dct[0], wordScore(dct[0], scores)] + wordsWithScore(dct[1:],scores)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n == 0:
        return []
    if n == 1:
        return L[0]
    if n > len(L):
        return "Error"
    return L[0] + take(n+1, L[1:]
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n == 0:
        return [0 + L[1:]]
    if L == []:
        return []
    if n > len(L):
        return "Error"
    return drop(n-1, L[1:])

