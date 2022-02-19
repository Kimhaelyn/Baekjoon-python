import sys

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline())) #input()은 느려서 시간초과되기 때문에 sys.stdin.readline() 사용

arr.sort()

for i in arr:
    print(i)
