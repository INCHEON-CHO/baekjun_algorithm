n, m = map(int, input().split())
l = [0]*(n+1)
d = [[0]*(n+1) for _ in range(n+1)]
c = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    l[i] = int(input())
def go(x,y):
    if y==0:
        return 0
    if x<=0:
        return -32768*101
    if c[x][y]:
        return d[x][y]
    c[x][y] = 1
    d[x][y] = go(x-1,y)
    sum = 0
    for k in range(x,0,-1):
        sum+=l[k]
        tmp = go(k-2,y-1) + sum
        if d[x][y]<tmp:
            d[x][y]=tmp
    return d[x][y]
print(go(n,m))

    
    