
def primetill():
    n=int(input('enter no'))
    for x in range(2,n+1):
        t=1
        y=x//2
        for i in range(2,y+1):
            if x%i==0:
                t=0
                break
        if t==1:
            print(x)


primetill()
