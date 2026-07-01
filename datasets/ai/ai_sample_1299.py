def printFibonacci(n):
    if n<0:
        print('Incorrect input')
    elif n==0:
        print(0)
    elif n==1:
        print(0,1)
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)