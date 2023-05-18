def prime_factors():

    num=int(input("enter a no."))
    
    prime_number=list()
    


    for i in range(1,int(num)):
        if num%i==0:
            factor_list1=list()
            for a in range(1,i+1):
                
                if i%a==0:
                    
                    factor_list1.append(a)

            if len(set(factor_list1))==2:
                prime_number.append(i)



    
    print(prime_number)


    
prime_factors()
