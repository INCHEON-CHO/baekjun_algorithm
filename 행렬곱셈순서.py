import sys
sys.setrecursionlimit(10000)
T = int(input())
d = [[0]*(T+1) for _ in range(T+1)]
a = [[0]*2 for i in range(T)]
def go(x,y):
    if d[x][y]: return d[x][y]
    if x==y:
        return 0
    ans = -1
    for k in range(x,y):
        t1 = go(x,k)
        t2 = go(k+1,y)
        if ans==-1 or ans>t1+t2+a[x-1][0]*a[k-1][1]*a[y-1][1]:
            ans = t1+t2+a[x-1][0]*a[k-1][1]*a[y-1][1]
    d[x][y]=ans
    return ans
for i in range(T):
    a[i][0], a[i][1] = map(int, input().split())

print(go(1,T))