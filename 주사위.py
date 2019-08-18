n = int(input())
l = list(map(int,input().split()))
idx = [1,2,4,3,1]
mini = min(l)
umini = -1
for i in range(4):
    tmp = min(l[0]+l[idx[i]]+l[idx[i+1]],l[5]+l[idx[i]]+l[idx[i+1]])
    if umini==-1 or umini>tmp:
        umini=tmp
dmini = -1
for i in range(4):
    if dmini==-1 or dmini > l[idx[i]]+l[idx[i+1]]:
        dmini = l[idx[i]]+l[idx[i+1]]
for i in range(1,5):
    tmp = min(l[0]+l[i], l[5]+l[i])
    if dmini>tmp:
        dmini = tmp

if n==1:
    print(sum(l)-max(l))
if n>=2:
    upside = umini*4 + ((n-2)**2)*mini + dmini*4*(n-2)
    side = dmini*4*(n-1) + 4*((n-2)*(n-1)*mini)
    print(upside+side)