#
# life.py - Game of Life lab
#
# Name: Nathan Carpenter    
# Pledge: I pledge my honor that I have abided by the stevens honors system. 
#

import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width" 
       This function should be used in 
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]   # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints a 2d list of lists
        A without spaces using sys.stdout.write
        which was imported with sys
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
       
def diagonalize(width,height):
    """ creates an empty board and ammends it into a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
     
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0      
 
    return A

def innerCells(width,height):
    """ returns an array of all live cells with a value of 1 except for
    the 1 cell wide border of 0 around the array
    """
    A = createBoard( width, height )
     
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0:
                A[row][col] = 0
            elif row == (height -1) or col == (width - 1):
                A[row][col] = 0
            else:
                A[row][col] = 1    
 
    return A

def randomCells(width,height):
    """ returns an array of random 0's and 1's
    and 0's except border is all 0 like innerCells  
    """
    A = createBoard( width, height )
     
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0:
                A[row][col] = 0
            elif row == (height -1) or col == (width - 1):
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])      
 
    return A

def copy(A):
    """ creates a new board and does a deep copy of
    array A to newA so values are saved not references
    """
    newA = createBoard(len(A[0]), len(A))

    for row in range(1, len(A)-1):
        for col in range(1,len(A[0])):
            newA[row][col] = A[row][col]
 
    return newA

def innerReverse(A):
    """creates a deep copy of A to newA and flips all the
    values from 1 to 0 or 0 to 1 except the outer border of 0
    """
    newA= copy(A)
    A = createBoard(len(A[0]), len(A))

    for row in range(1, (len(A))-1):
        for col in range(1,len(A[0])-1):
                if newA[row][col] == A[row][col]:
                    A[row][col] = 1
                else:
                    A[row][col] = 0
    return A

def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    newA = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if countNeighbors(row,col,A) <= 1:
                newA[row][col] = 0
            elif countNeighbors(row,col,A) == 3:
                newA[row][col] = 1
            elif countNeighbors(row,col,A) > 3:
                newA[row][col] = 0
    return newA
   

def countNeighbors(row,col,A):
    """returns the number of live neighbors for a
    cell in the board A at a particular row and col.
    """
    x=0
    if A[row-1][col-1]==1:
        x+=1
    if A[row][col-1]==1:
        x+=1
    if A[row+1][col-1]==1:
        x+=1
    if A[row-1][col]==1:
        x+=1
    if A[row+1][col]==1:
        x+=1
    if A[row-1][col+1]==1:
        x+=1
    if A[row][col+1]==1:
        x+=1
    if A[row+1][col+1] ==1:
        x+=1
    return x
