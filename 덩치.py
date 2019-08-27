n = int(input())
D = [[0,0] for _ in range(n)]
for i in range(n):
    D[i][0], D[i][1] = map(int, input().split())

l = [1]*n
for i in range(n):
    for j in range(n):
        if D[i][0]<D[j][0] and D[i][1]<D[j][1]:
            l[i]+=1
for i in range(n):
    print(l[i],end=' ')