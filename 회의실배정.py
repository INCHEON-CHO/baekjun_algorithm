T = int(input())
l = [[0,0] for i in range(T)]
for i in range(T):
    l[i][0], l[i][1] = map(int, input().split())


l = sorted(l,key = lambda x:(x[1],x[0]))

tmp = l[0]
ans = 1
for i in range(1,T):
    if tmp[1]<=l[i][0]:
        tmp=l[i]
        ans+=1
print(ans)