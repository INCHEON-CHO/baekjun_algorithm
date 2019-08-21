N = int(input())

Tree = []
for i in range(N):
    level = list(map(int,input().split()))
    Tree.append(level)

for i in range(N-1,0,-1):
    for j in range(i):
        Tree[i-1][j]+=max(Tree[i][j],Tree[i][j+1])

print(Tree[0][0])