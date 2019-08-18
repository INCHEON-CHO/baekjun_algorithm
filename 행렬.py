
N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    a.append(list(input()))
for i in range(N):
    b.append(list(input()))

cnt=0
for i in range(N-2):
    for j in range(M-2):
        if a[i][j]!=b[i][j]:
            for k in range(3):
                for l in range(3):
                    a[i+k][j+l] = str(1-int(a[i+k][j+l]))
            cnt+=1
bo=0
for i in range(N):
    for j in range(M):
        if a[i][j]!=b[i][j]:
            print(-1)
            bo=1
            break
    if bo==1:
        break
if bo==0:
    print(cnt)
