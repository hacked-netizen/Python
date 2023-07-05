# -*- coding: utf-8 -*-
def calc(a,b):
    x=int(input('''enter the operation to perform
                   1. Addition
                   2. Subtraction
                   3. Multiplication
                   4. Division'''))
    if x==1:
        print(a+b)
    elif x==2:
        print(a-b)
    elif x==3:
        print(a*b)
    elif x==4:
        print(a/b)
    else:
        print("Enter a valid input")
        
        
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))

calc(a, b)