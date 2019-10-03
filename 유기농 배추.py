import sys
sys.setrecursionlimit(10**6)
T = int(input())

def go(x,y):
    if arr[x][y]!=0 and c[x][y]!=1:
        c[x][y]=1
        go(x-1,y)
        go(x+1,y)
        go(x,y-1)
        go(x,y+1)

for _ in range(T):
    m,n,k = map(int,input().split())
    cnt = 0
    arr = [[0]*(m+2) for _ in range(n+2)]
    c = [[0]*(m+2) for _ in range(n+2)]
    for _ in range(k):
        i, j = map(int, input().split())
        arr[j+1][i+1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if arr[i][j]==1 and c[i][j]==0:
                go(i,j)
                cnt+=1
    print(cnt)

