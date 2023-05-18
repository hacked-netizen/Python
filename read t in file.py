f= open("student.txt",'r+')
x=f.read()
f.write("parth")
f.close()

count=0


for i in x:
    if i=='t':
        count+=1
print(x)
print(count)
