
def sof(x,n):
    import math
    if n==0:
        return 1
    else:
        return (x**n/math.factorial(n))+ sof(x,n-1)


def main():
    
    n=int(input('enter a number'))
    b=int(input('enter a power'))

    print(sof(n,b))
    

    


if __name__=='__main__':
    main()
     
'''    def power(x,n):
        if n==0:
            return 1
        else:
            return x*power(x,n-1)


    def factorial(n):
        if n==0:
            return 1
        else:
            return n*factorial(n-1)'''
