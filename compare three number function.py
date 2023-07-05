# -*- coding: utf-8 -*-4
def compare(a,b,c):
    if a<b and a<c:
        return str(a)+" is smallest "
    if b<a and b<c:
        return str(b)+" is smallest "
    if c<a and c<b:
        return str(c)+" is smallest "
    else:
        return "all three numbers are equal"
        
    

x=float(input("Enter the first number"))
y=float(input("Enter the second number"))
z=float(input("Enter the third number"))

print(compare(x,y,z))
