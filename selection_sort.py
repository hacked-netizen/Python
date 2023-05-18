def selectionsort(l):
    # scan slices l[0:len(l)], l[1:len(l)], ...
    for start in range(len(l)):
        # find minimum value in slice . . .
        minpos = start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i

        # . . . and move it to start of slice
        (l[start],l[minpos])=(l[minpos],l[start])



list1=[4,5,85,96,58,14,2,36,78,91,92,225]
print(list1)
selectionsort(list1)
print(list1)
