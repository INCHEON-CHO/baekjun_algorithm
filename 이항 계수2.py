N, K = map(int, input().split())
K = min(K, N-K)

if K==0:
    print(1)
else:
    mo = 1
    so = 1
    for i in range(K):
        mo *= N-i
        so *= i+1
    print((mo//so)%10007)