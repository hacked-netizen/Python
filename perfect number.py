def perfect_no():

    num=int(input("enter a no."))
    
    prime_number=list()
    sum1=0


    for i in range(1,int(num)):
        if num%i==0:
            prime_number.append(i)
            sum1+=i



    
    print(prime_number)

    if sum1==num:
        print("it is perfect number")


perfect_no()
