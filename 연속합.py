N = int(input())
line = list(map(int,input().split()))

D = [0]*(N+1)
for i in range(N-1,-1,-1):
    D[i]=max(D[i+1]+line[i],line[i])

print(max(D[0:-1]))