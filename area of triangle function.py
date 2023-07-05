# -*- coding: utf-8 -*-4
import math
def area(a,b,c):
    '''
    using herons formula to calculate area
    area=(s(s-a)(s-b)(s-c))^0.5
    s=(a+b+c)/2
    
    '''
    if (a+b>c) and (b+c>a) and (c+a>b):
        s=(a+b+c)/2
        heron=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return "Area of the triangle is "+str(heron)
    else:
        return "Enter a valid triangle dimensions"
        
    

x=float(input("Enter the first sidelength"))
y=float(input("Enter the second sidelength"))
z=float(input("Enter the third sidelength"))

print(area(x, y, z))