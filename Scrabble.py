'''
Created on February 9th, 2022

@author: Nathan Carpenter
I pledge my honor that I have abided by the stevens honor system
'''
import sys
from cs115 import reduce
sys.setrecursionlimit(10000)

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]
Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", "spam", "spammy", "zzyzva"]

def letterScore(letter, scrabbleScores):
    """returns the integer value of any letter in the game scrabble"""
    if scrabbleScores == []:
        return 0
    if scrabbleScores[0][0]== letter:
        return scrabbleScores[0][1]
    return letterScore(letter, scrabbleScores[1:])

def wordScore(s, scrabbleScores):
    """returns value of a word"""
    def wordScore_helper(s, scrabbleScores):
        """returns the point value for the first letter, plus all the previous ones, + the word with the first letter removed"""
        if s == "":
            return []
        return [letterScore(s[0], scrabbleScores)] + wordScore_helper(s[1:], scrabbleScores)
    return reduce(lambda x,y: x+y, wordScore_helper(s, scrabbleScores))

def is_word_possible(word, rack):
    """returns true if you can make a word in the dictionary and false if you cant"""
    new_rack = list(rack)
    if word == "":
        return True
    if word[0] in rack:
        new_rack.remove(word[0])
        return is_word_possible(word[1:], new_rack)
    else:
        return False

def list_of_words(rack, Dictionary):
    """returns a list of all the possible words you can make with your rack of letters"""
    if Dictionary == "" or Dictionary == []:
        return []
    if is_word_possible(Dictionary[0], rack) == True:
        return [Dictionary[0]] + list_of_words(rack, Dictionary[1:]) 
    return list_of_words(rack, Dictionary[1:]) 



def map_score(words):
    """applies the wordScore function to the list of all the words you can make"""
    if words == []:
        return []
    return [[words[0], wordScore(words[0], scrabbleScores)]] + map_score(words[1:])

def scoreList(rack):
    """returns a list of all the possible words you can make and their scores"""
    return map_score(list_of_words(rack, Dictionary))

    

def bestWord(rack):
    """returns the best possible word you can make with your letters. If no word is possible, returns an empty string and a 0"""
    new_list = scoreList(rack)
    def rate(new_list):
        """this checks to see what word in wordList had the highest score and returns it"""
        if new_list == [] or new_list == "":
            return ["", 0]
        if len(new_list) <= 1:
            return new_list[0]
        if new_list[0][1] <= new_list[1][1]:
            return rate(new_list[1:])
        new_list.pop(1)
        return rate(new_list[0:])
    return rate(new_list)


    


  

