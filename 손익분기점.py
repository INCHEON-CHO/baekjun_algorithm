l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])

if l[2]<=l[1]:
    print(-1)
else:
    print(int(l[0]/(l[2]-l[1]))+1)