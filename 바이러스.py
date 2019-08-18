import queue
m = int(input())
n = int(input())

c = [0]*m
l = [[] for i in range(m)]
q = queue.Queue()

cnt = 0
for i in range(n):
    a1 ,a2 = map(int, input().split())
    l[a1-1].append(a2)
    l[a2-1].append(a1)

q.put(1)
c[0]=1
while (q.qsize()):
    x = q.get()
    cnt+=1
    for i in range(len(l[x-1])):
        if c[l[x-1][i]-1]==0:
            q.put(l[x-1][i])
            c[l[x-1][i]-1]=1

print(cnt-1)