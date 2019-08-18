import sys
sys.setrecursionlimit(10000)
T = int(input())
s = []
d = [[]]

def go(x,y):
    if x==y:
        return 0
    if d[x][y]!=-1:
        return d[x][y]
    for k in range(x,y):
        if d[x][y]==-1 or d[x][y]>go(x,k)+go(k+1,y)+s[y]-s[x-1]:
            d[x][y] = go(x,k)+go(k+1,y)+s[y]-s[x-1]
    return d[x][y]
for _ in range(T):
    n = int(input())
    l = list(map(int,input().split()))
    s = [0]*501
    d = [[-1]*501 for i in range(501)]
    for i in range(1,n+1):
        s[i]=s[i-1]+l[i-1]
    print(go(1,n))
