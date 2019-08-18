pel = input()
n = len(pel)
d = [0]*(n+1)
a = [[0]*n for i in range(n)]

for i in range(n):
    a[i][i]=1
for i in range(n-1):
    if pel[i]==pel[i+1]:
        a[i][i+1]=1
for k in range(2,n):
    for i in range(n-k):
        j = i+k
        if pel[i]==pel[j] and a[i+1][j-1]:
            a[i][j]=1

d[0]=0
for i in range(1,n+1):
    d[i] = -1
    for j in range(1,i+1):
        if a[j-1][i-1]:
            if d[i]==-1 or d[i]>d[j-1]+1:
                d[i] = d[j-1]+1
print(d[n])