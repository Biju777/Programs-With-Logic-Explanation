'''
author =  Biju
Title = Fibonacci
'''
import time

def fiboIterative(n):
    prevNum = 0
    currentNum = 1
    for i in range(1, n):
        prevPrevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prevPrevNum
    return currentNum


# For Fibonacci Recursive method is not good so we try Iterative Method
def fiboRecursive(n):
    if n==0:
        return 0
    
    elif(n==1):
        return 1
    
    else:
        return fiboRecursive(n-1) + fiboRecursive(n-2)

if __name__ == '__main__':
    num = int(input("Enter a number:"))
    init = time.time()
    # print(f"Using recursice value of fib {num} is {fiboRecursive(num)}")
    print(f"Using Iterative value of fib {num} is {fiboIterative(num)}")
    print(f"It took {time.time() - init} seconds")
    