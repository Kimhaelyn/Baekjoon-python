N=int(input())

people = []

for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for c in people: #c=현재 사람
    rank=1

    for n in people: #n=다음 사람
        if(c[0]!=n[0]) & (c[1]!=n[1]): #자신은 제외하고 비교
            if(c[0]<n[0]) & (c[1]<n[1]): #c[0], n[0]은 몸무게고 c[1], n[1]은 키.
                rank += 1 #몸무게와 키가 모두 큰 경우 -> 나보다 덩치 큰 사람의 수만큼 +1

    print(rank)
