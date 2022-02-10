x=int(input())
line=1 #각 대각선

while x>line: #변수 x가 대각선 line의 수보다 작아질 때, 해당하는 대각선에 찾고있는 변수 x가 있는 것이다.
    x-=line
    line+=1

if line%2==0: #line이 짝수면
    a=x #분자는 1부터 n까지 늘어난다. 
    b=line-x+1 #분모는 n부터 1까지 줄어든다.
else: #line이 홀수면
    a=line-x+1 #분자는 n부터 1까지 줄어든다.
    b=x #분모는 1부터 n까지 늘어난다.

print("{}/{}".format(a,b))
