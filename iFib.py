def iFib(n):
    prev = 0
    cur = 1
    summ = 0
    for i in range(0, n):
        if n == 0 or n == 1:
            return n
        else:
            prev = cur
            cur = summ
            summ = prev + cur
            print(summ)
    return summ

    
        
