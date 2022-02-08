array=[] #빈 배열 생성

for i in range(10): 
    n=int(input())
    array.append(n%42) #배열 마지막에 원소 추가

array=set(array) #set 함수로 중복되는 수를 제거한다.
print(len(array))
