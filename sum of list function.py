def listsum():
    num=int(input("enter no. of terms"))
    list1=[]
    while num>0:
        a=input("enter a list")
        list1.append(a)
        num-=1
    count=0
    for i in list1:
        count+=int(i)
    print(count)

listsum()
