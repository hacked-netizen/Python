def longstring():
    u=input("enter a string")
    a=u.split()
    long=""
    for i in a:
        
        if len(i)>len(long):
            long=i
        else:
            continue

    print(long)



longstring()
