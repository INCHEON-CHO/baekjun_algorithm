n, won = map(int,input().split())
l = [0]*n
ans = 0
for i in range(n):
    l[i]=int(input())
for i in range(n-1,-1,-1):
    ans+=won//l[i]
    won%=l[i]
print(ans)
