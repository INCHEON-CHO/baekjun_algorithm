n, k = map(int, input().split())
l = []
for i in range(n):
    l.append(int(input()))
d = [0]*(k+1)
d[0]=1
for i in range(n):
    for j in range(k+1):
        if j-l[i]>=0:
            d[j]+=d[j-l[i]]
print(d[k])
