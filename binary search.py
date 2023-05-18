def bsearch(seq,v,l,r):
    #search for v in seq[l:r], seq is sorted

    if r-l == 0:
        return False
    mid = (l+r)//2
    if v==seq[mid]:
        return True

    if v<seq[mid]:
        return bsearch(seq,v,l,mid)

    else:
        return bsearch(seq,v,mid+1,r)

list1=[1,85,47,50,451,63,78,95,65,41,75,84,2,5,56,314,87,85529,4]
list1.sort()
print(bsearch(list1,85529,0,len(list1)))
