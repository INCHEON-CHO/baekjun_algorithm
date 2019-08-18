n = int(input())
mat = []
for i in range(n):
    l = input().split()
    for j in range(n):
        l[j] = int(l[j])
    mat.append(l)
d = [[0]*n for i in range(n)]
d[0][0]=1
for i in range(n):
    for j in range(n):
        if mat[i][j]==0:
            continue
        if i+mat[i][j]<n:
            d[i+mat[i][j]][j]+=d[i][j]
        if j+mat[i][j]<n:
            d[i][j+mat[i][j]]+=d[i][j]
print(d[n-1][n-1])

