def fibo(n):
    if n>=3:
        #print(fibo(n-1) + fibo(n-2))
        return fibo(n-1) + fibo(n-2)
    elif n==0:
        #print(0)
        return 0
    elif n==1:
        #print(1)
        return 1
    elif n==2:
        #print(0)
        #print(1)
        return 1
    else:
        print("wrong input type")


print(fibo(9))