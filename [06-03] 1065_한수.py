n=int(input())
hansu=0

for i in range(1, n+1):
    if i<100: #1부터 99까지의 수는 모두 등차수열이다.
        hansu += 1

    else:
        a=list(map(int, str(i)))#list(map(int, 리스트): 수를 하나씩 나눔.
        if a[0]-a[1]==a[1]-a[2]:
            hansu+=1

print(hansu)
