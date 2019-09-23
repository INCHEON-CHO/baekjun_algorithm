N = int(input())
arr = ['0'*(N+2)]
for i in range(N):
    arr.append('0'+input()+'0')
arr.append('0'*(N+2))
c = [[0]*(N+2) for _ in range(N+2)]

def go(x,y):
    if arr[x][y]=='0' or c[x][y]==1:
        return 0
    if arr[x][y]=='1' and c[x][y]==0:
        c[x][y]=1
        return 1+go(x,y+1)+go(x,y-1)+go(x-1,y)+go(x+1,y)

cnt = 0
ans = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j]=='1' and c[i][j]==0:
            cnt+=1
            ans.append(go(i,j))
print(cnt)
ans.sort()
for i in ans:
    print(i)