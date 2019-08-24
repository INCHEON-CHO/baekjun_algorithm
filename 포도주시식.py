N = int(input())
D = [0]*10001
grape =[0]*(N+1)
for i in range(1,N+1):
    grape[i]=int(input())
if N==1:
    print(grape[1])
else:
    D[1] = grape[1]
    D[2] = grape[1]+grape[2]
    for i in range(3,N+1):
        D[i] = max(grape[i]+grape[i-1]+D[i-3],grape[i]+D[i-2],D[i-1])
    print(D[N])