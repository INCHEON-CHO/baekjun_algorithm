'''T = int(input())

def gcd(m,n):
    while(n!=0):
        tmp = m%n
        m=n
        n=tmp
    return m

for i in range(T):
    M,N,x,y = map(int,input().split())
    if (M<N):
        M,N=N,M
        x,y=y,x
    s=x
    c=0
    while(s<=M*N/gcd(M,N)):
        if (s%N==y):
            print(s)
            c=1
            break
        s+=M
    if c==0:
        print(-1)
'''
for i in range(int(input())):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = x
    while s < M*N:
        if s % N == y:
            print(s+1)
            break
        s += M
    if s % N != y:
        print(-1)