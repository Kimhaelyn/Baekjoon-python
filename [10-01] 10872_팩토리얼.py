def Fact(n):
    res=1
    if n>0:
        res=n*Fact(n-1)
    return res

n=int(input())
print(Fact(n))
