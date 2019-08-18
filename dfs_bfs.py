import queue

q = queue.Queue()

n,m,init = map(int,input().split())
c=[0]*n
vec = [[] for i in range(n)]

for i in range(m):
    i1, i2 = map(int,input().split())
    vec[i1-1].append(i2-1)
    vec[i2-1].append(i1-1)

for i in range(n):
    vec[i].sort()

def dfs(x):
    if c[x-1]==1: return
    c[x-1]=1
    print(x,end=' ')
    for i in range(len(vec[x-1])):
        y=vec[x-1][i]
        dfs(y+1)
dfs(init)
print()

c = [0]*n

def bfs(x):
    q.put(x)
    c[x-1]=1
    while(q.qsize()):
        y = q.get()
        print(y, end=' ')
        for i in range(len(vec[y-1])):
            if c[vec[y-1][i]]!=1:
                q.put(vec[y-1][i]+1)
                c[vec[y-1][i]]=1

bfs(init)