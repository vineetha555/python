from ast import Num


def factorial(num):
    if num==1:
        return 1
    else:
        return(num * factorial(num-1))
num=5
print('factorial of 5 is',factorial(num))





