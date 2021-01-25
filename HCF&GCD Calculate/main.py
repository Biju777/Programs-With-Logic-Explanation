'''
Author = Biju
Date = 2021/01/09
Purpose = Highest commen factor  90&30 2*3*5 = 30 and 30*3 = 90 and 30 / 2,3,5
'''

Number1 = int(input("Enter frist number:\n"))
Number2 = int(input("Enter second number:\n"))

if Number1<Number2:
    Minimum = Number1
else:
    Minimum = Number2

for i in range(1, Minimum+1):
    if Number1%i==0 and Number2%i==0:
        HCF = i

print(f"The HCF of {Number1} and {Number2} is {HCF}")