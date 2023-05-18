def palindrome(a):n #a list is passed into the string
    n=len(a)
    if n==0:
        return ""
    else:
        return a[n-1]+palindrome(a[0:n-1])'''the function ids called recusively
                                            to inverse the string'''
