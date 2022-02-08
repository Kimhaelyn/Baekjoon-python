a=int(input())
b=int(input())
c=int(input())

res=list(str(a*b*c)) #a*b*c의 값을 문자열로 변환하고 list를 사용해 각 문자를 요소로 가지는 리스트로 변환한다.
for i in range(10):
    print(res.count(str(i))) #count로 리스트의 문자 개수를 세서 출력한다.
