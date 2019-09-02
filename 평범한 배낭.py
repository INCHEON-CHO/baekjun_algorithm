n, k = map(int, input().split())

D = [[0]*100001 for i in range(101)]
w = [0]*101
v = [0]*101
for i in range(1,n+1):
    w[i], v[i] = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,k+1):
        D[i][j] = D[i-1][j]
        if j-w[i]>=0:
            D[i][j] = max(D[i][j], D[i-1][j-w[i]]+v[i])

print(D[n][k])
