n=int(input())
num=list(map(int, input().split())) #list(map(함수, 리스트)): 리스트 요소를 int로 변환해줌.
                                                            #문자열.split(): 문자열을 나눠서 리스트로 만들어줌.

print(min(num), max(num))
