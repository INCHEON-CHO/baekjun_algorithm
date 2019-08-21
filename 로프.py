N = int(input())
line = []
for _ in range(N):
    line+=[int(input())]
line.sort()
MAXKG = 0
for i in range(N):
    if MAXKG<line[i]*(N-i):
        MAXKG=line[i]*(N-i)
print(MAXKG)