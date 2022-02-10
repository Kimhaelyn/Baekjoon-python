n=int(input())
arr = map(int, input().split()) #문자열을 일정한 규칙으로 나눠(split) 함수로 처리(map)

sosu=0

for num in arr:
    error=0
    if num>1:
        for i in range(2, num):
            if num%i == 0:
                error+=1

        if error==0:
            sosu+=1

print(sosu)
