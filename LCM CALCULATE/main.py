'''
Author = Biju
Date = 2021/01/09
'''

num1 = int(input("Enter frist number:\n"))
num2 = int(input("Enter second number:\n"))

Maximum = max(num1,num2)

while(True):
    if Maximum%num1==0 and Maximum%num2==0:
        break
    Maximum = Maximum+1

print(f"The LCM of {num1} and {num2} is {Maximum}")