import random

print("do you want roll a dice")
x=input("yes or no")
y=random.randint(1,6)

if x=="yes":
    print("your dice number is:",y)

if x=="no":
    exit()
