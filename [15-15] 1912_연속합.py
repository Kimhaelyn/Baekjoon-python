n=int(input())

a=list(map(int, input().split())) #a에 list로 숫자를 받는다.
sum=[a[0]] #sum이라는 새로운 리스트를 만들고 sum의 0번째 인덱스에 비교를 위해 a[0]을 넣는다.
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i+1], a[i+1])) #수를 비교하여 더 큰 숫자를 sum 리스트에 넣는다.
print(max(sum))
