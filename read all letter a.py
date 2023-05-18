a=open("file1.txt","r+")
b=open("names1.txt","w")
def split1(word): 
    return [char for char in word]  
while 1:
    line=a.readline()
    if not line:
        break
    else:
        c=line.split()
        d=list(c)
        for l in d:
            e=split1(l)
            f=list(e)
            for i in f:
                if i=='a':
                    b.write(line)
b.close()
a.close()
