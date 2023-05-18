def charcheck():
    
    fed=input("enter a string")
    upcount=0
    lowcount=0
    for i in fed:
        if i.isupper():
            upcount+=1
        if i.islower():
            lowcount+=1
        
    print("number of lower character is: ",lowcount)
    print("number of upper character is: ",upcount)




charcheck()
