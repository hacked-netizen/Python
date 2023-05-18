import pickle
file=open('data.dat','wb')

while True:
    x=int(input("enter a number"))
    pickle.dump(x,file)
    ans=input("want to enter more number?")
    if ans.upper()=='N':
        break


file.close()
file=open('data.dat','rb')

try:
    while True:
        g=pickle.load(file)
        print(g)

except EOFError:
    pass

file.close()
