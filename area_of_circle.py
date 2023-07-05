# -*- coding: utf-8 -*-
import math
def area(r):
    '''
    function to find area using formula
    area=pi*radius*radius

    '''
    if r>=0:
        return "Area is "+str(r*r*math.pi)
    else:
        return "Enter a valid radius"
    

radius=int(input("Enter the radius of the circle"))
print(area(radius))