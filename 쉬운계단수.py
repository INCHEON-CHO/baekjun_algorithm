N = int(input())
MOD = 1000000000
D = [[0]*101 for _ in range(10)]
for i in range(10):
    D[i][1]=1
for k in range(2,101):
    for i in range(10):
        if i==0:
            D[i][k] = D[i+1][k-1]
        elif i==9:
            D[i][k] = D[i-1][k-1]
        else:
            D[i][k] = (D[i-1][k-1] + D[i+1][k-1])%MOD
ans = 0
for i in range(1,10):
    ans+=D[i][N]

print(ans%MOD)