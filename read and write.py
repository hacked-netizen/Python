F1 = open('file.txt','r')
f2 = open('file2.txt','a')

line=F1.readline()

while line == '\0':
    f2.write(line)
    line = F1.readline()

F1.close()
f2.close()
