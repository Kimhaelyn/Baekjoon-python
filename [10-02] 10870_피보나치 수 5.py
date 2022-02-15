def Fibonacci(n):
    if n>=2:
        res=Fibonacci(n-1)+Fibonacci(n-2)
    elif n==0:
        res=0
    elif n==1:
        res=1
    return res

n=int(input())
print(Fibonacci(n))
