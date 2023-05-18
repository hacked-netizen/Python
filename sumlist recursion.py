def sumlist(l):
    if l==[]:
        return 0
    else:
        return l[0]+sumlist(l[1:])

print(sumlist([1,2,3,4,5,6,7,8,9]))
