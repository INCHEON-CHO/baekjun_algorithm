n, m = map(int,input().split())
a = []
for i in range(n):
    b = input().split()
    for j in range(m):
        b[j] = int(b[j])
    a.append(b)
d = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1]) + a[i-1][j-1]
print(d[n][m])