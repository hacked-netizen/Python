def sumofnum(n):
    if lenght(n)==0:
        return 0
    else:
        return n[0]+sumofnum(n-1)


def main():
    a=int(input('enter a number'))
    

    print(sumofnum(a))


if __name__=='__main__':
    main()
    


