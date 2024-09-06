def fibo(n):
    if n==2:
        return 1+fibo(n-1)
    elif n==1:
        return 0

    k = fibo(n-1)+fibo(n-2)
    return k
    #print(n)

print(fibo(5))