def threepart():
    u=input("enter a string")
    n=len(u)
    if n<3:
        print("string should be atleast 3 character long")
    else:
        a=u[:1]
        b=u[1:2]
        c=u[2:n]
        print(a)
        print(b)
        print(c)



threepart()
