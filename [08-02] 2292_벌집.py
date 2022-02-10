n=int(input())

bee=1 #벌집 개수.
count=1

while n>bee:
    bee += 6*count #벌집이 6의 배수로 증가함
    count += 1 #반복문 반복 횟수

print(count)
