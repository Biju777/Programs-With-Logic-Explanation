'''
Author = Biju
Date = 2021/01/09
Purpose = Factorial
'''

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)

def factorialTrailingZeros(number):
    i = 5
    count = 0
    while(number//i !=0):
        count += int(number/i)
        i = i*5
    return count

if __name__ == "__main__":
    number = int(input("Enter a number:\n"))
    # fac = factorial(number)
    # print(f"The factorial is {fac}")
    print(f"The factroialTrailingZeros is {factorialTrailingZeros(number)}")


print(17*16*15*13*12*11*10*9*8*7*6*5*4*3*2*1)
