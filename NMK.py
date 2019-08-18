N, M, K = map(int, input().split())
if N>=M+K-1 and N<=M*K:
    l = list(range(1,N+1))
    g = [0,K]
    N-=K
    M-=1
    if M==0: gs=1
    else : gs = N//M
    if M==0: r=0
    else : r = N%M
    for i in range(M):
        if r>0:
            g.append(g[-1]+gs+1)
        else:
            g.append(g[-1]+gs)
        if (r>0): r-=1
    for i in range(len(g)-1):
        b = sorted(l[g[i]:g[i+1]], reverse=True)
        for i in b:
            print(i,end=" ")
else:
    print(-1)
