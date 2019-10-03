n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
c = [[0]*m for _ in range(n)]
queue = [[0,0]]
cal = [[0,1],[1,0],[0,-1],[-1,0]]
c[0][0]=1
cnt=0
while len(queue):
    x,y = queue.pop(0)
    if x==n-1 and y==m-1:
        print(c[x][y])
        break
    for i in range(4):
        a = x+cal[i][0]
        b = y+cal[i][1]
        if a>=0 and a<=n-1 and b>=0 and b<=m-1:
            if c[a][b]==0 and arr[a][b]=='1':
                c[a][b] = 1+c[x][y]
                queue.append([a,b])
