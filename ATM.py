T = int(input())

l = input().split()
for i in range(T):
    l[i] = int(l[i])
l.sort()
ans = 0
ansl = []
for i in range(T):
    ans+=l[i]
    ansl.append(ans)
print(sum(ansl))