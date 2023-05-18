def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)


def main():
    a=int(input('enter a number'))
    b=int(input('enter a power'))

    print(power(a,b))


if __name__=='__main__':
    main()
    
