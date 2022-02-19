n=int(input())

num=[]
for i in str(n):
    num.append(int(i))

num.sort(reverse=True)

for i in num:
    print(i, end='')
