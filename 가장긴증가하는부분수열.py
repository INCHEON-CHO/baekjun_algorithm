N = int(input())
l = list(map(int,input().split()))

D = [0]*1001
ans = 0

for i in range(N):
    here = 0
    for j in range(1,i+1):
        if l[i]>l[j-1]:
            here = max(here, D[j])
    D[i+1] = here+1
    ans = max(D[i+1],ans)
print(ans)
