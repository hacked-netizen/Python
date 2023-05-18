def evennum(a):
    if a%2==0:
        return a
    else:
        return 0
    


l=[1,3,4,56,67,87,90,87,87,88,645,66,44,36,24,52,678,35,76,567,876,312,864,246]

l.sort(key=evennum,reverse=True)
b=l
c=[i for i in l if i%2==0]
