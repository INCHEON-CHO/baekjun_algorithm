N = int(input())
line = [[0,0] for _ in range(N)]
for i in range(N):
    line[i][0], line[i][1] = map(int, input().split())
line = sorted(line, key=lambda x:x[0])
D = [0]*(N+1)
ans=0

for i in range(1,N+1):
    cnt=0
    for j in range(1,i):
        if line[i-1][0]>line[j-1][0] and line[i-1][1]>line[j-1][1]:
            cnt=max(cnt,D[j])
    D[i] = cnt+1
    ans = max(ans,D[i])
print(N-ans)
