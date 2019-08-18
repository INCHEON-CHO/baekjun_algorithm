import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
d = [[-1]*m for i in range(n)]

lx = [0,0,-1,1]
ly = [1,-1,0,0]
d[n-1][m-1]=1
def go(x,y):
    if x==n-1 and y==m-1:
        return 1
    if d[x][y]!=-1:
        return d[x][y]
    ans = 0
    for i in range(4):
        rx = x + lx[i]
        ry = y + ly[i]
        if rx<0 or rx>=n or ry<0 or ry>=m:
            continue
        if l[x][y]>l[rx][ry]:
            ans += go(rx,ry)
    d[x][y]=ans
    return ans
print(go(0,0))