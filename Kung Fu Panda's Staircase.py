#Name:Nathan Carpenter
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.

################
# Kung Fu Panda has a number of staircases he needs to climb.
# He likes to climb each staircase 1, 2, or 3 steps at a time.
# Being a very precocious character, he wonders how many ways
#there are to reach the top of the staircase. Your help is needed here.
################

# 1. Write a recursive function KFP_slow that will take as an input a positive integer
#    denoting the number of stairs and will return the number of ways Kung Fu Panda can climb those stairs.


def KFP_slow(n):
    """Function receives an int and returns the total number of ways KFP can climb that many stairs."""
    if n <=1:
        return 1
    elif n ==2:
        return 2
    elif n == 3:
        return 4
    else:
        steps
        return 1+((n-1)+(n-2))
   
   

print(KFP_slow(5))
print(KFP_slow(30))


# 2. Use memoization to speed up your solution of KFP_slow.
memo = {5:13, 3:4}
def KFP_fast(n):
    pass        

print(KFP_fast(5))
print(KFP_fast(30))

