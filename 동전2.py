n, k = map(int, input().split())
s = set()
for i in range(n):
    s.add(int(input()))
s = list(s)
s.sort()

d = [-1]*(k+1)
d[0]=0
for i in range(len(s)):
    for j in range(1,k+1):
        if j-s[i]>=0 and d[j-s[i]]!=-1:
            if d[j]==-1 or d[j]>d[j-s[i]]+1:
                d[j] = d[j-s[i]]+1
print(d[k])