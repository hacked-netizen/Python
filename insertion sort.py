def insertionsort(seq):
    for sliceEnd in range(len(seq)):
        # Build longer and longer sorted slices
        #in each iteration seq[0:sliceEnd] already sorted

        # Move first element after the sorted slice left
        # till it is in the correct place
        pos=sliceEnd
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1

list1=[4,5,85,96,58,14,2,36,78,91,92,225]
print(list1)
insertionsort(list1)
print(list1)
