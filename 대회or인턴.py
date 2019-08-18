M, N, K = map(int, input().split())
ans = 0
while M>=2 and N>=1 and M+N>=K+3:
    ans+=1
    M-=2
    N-=1
print(ans)