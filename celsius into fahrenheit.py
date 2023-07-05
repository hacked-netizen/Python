# -*- coding: utf-8 -*-4
def convert(c):
    '''
    using formula
    (c*9/5)+32=f
    
    '''
    f=(c*(9/5))+32
    return f
        
    

x=float(input("Enter the temperature(in celsius) to convert"))

print("In fahrenheit it is ",convert(x))