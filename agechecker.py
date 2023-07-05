# -*- coding: utf-8 -*-
def agechecker(a):
    '''
    function to validate age

    '''
    if a>=18:
        return "Age is valid"
    else:
        return "Age is not valid"
    
#driver code
year=int(input("Enter your age"))
print(agechecker(year))
