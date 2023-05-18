def sumoflist(n):
    a=len(n)
    if a==0:
        return 0
    else:
        return n[0]+sumoflist(n[1:a])



n=[1,2,3,4,5,6,6]

print(sumoflist(n))
