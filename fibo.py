def fibo(n):
    if n==0:
        print(0)
    elif n==1:
        print(0)
        print(1)

    a=0
    b=1
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c


fibo(10)