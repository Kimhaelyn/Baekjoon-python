n=int(input())
arr=input()
res=0

for i in range(n): //n개의 숫자를 문자열로 입력받은 뒤 하나씩 분리해서 변수 i로 꺼낸다.
    res+=int(arr[i]) //문자열을 int 함수로 변환하여 res에 더한다.

print(res)
