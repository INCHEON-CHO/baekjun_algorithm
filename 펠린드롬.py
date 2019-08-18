n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])
d = [[-1]*n for i in range(n)]

for i in range(n):
    d[i][i]=1
for i in range(n-1):
    if d[i]==d[i+1]:
        d[i][i+1]=1
    else:
        d[i][i+1]=0
for k in range(3,n+1):
    for i in range(n-k+1):
        j = i+k-1
        if (l[i]==l[j]) and d[i+1][j-1]:
            d[i][j]=1
        else:
            d[i][j]=0
m = int(input())
for i in range(m):
    S, E = map(int,input().split())
    print(d[S-1][E-1])