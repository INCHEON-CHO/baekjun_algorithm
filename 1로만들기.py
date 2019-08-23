N = int(input())

D = [0]*(1000001)
D[2]=1
for i in range(3,N+1):
    if i%3==0:
        D[i] = min(D[i-1]+1, D[i//3]+1)
    elif i%2==0:
        D[i] = min(D[i-1]+1, D[i//2]+1)
    else:
        D[i] = D[i-1]+1

print(D[N])