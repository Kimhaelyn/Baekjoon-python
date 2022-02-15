n=int(input())

for i in range(n+1):
    num=sum((map(int, str(i)))) #i의 각 자릿수를 더함
    hap = i + num #분해합 = 생성자 + 각 자릿수의 합

    if hap==n:
        print(i)
        break
    if i==n: #생성자가 없는 경우
        print(0)
