
def climbStairs(n):
    distinctways = 0
    step1=1
    step2=2

    if n ==0:
        return 0
    elif n == 1:
        return 1


    while n>=2:
        if climbStairs(n-1)
            distinctways = distinctways+1
        n-=1


    return distinctways


print(climbStairs(3))