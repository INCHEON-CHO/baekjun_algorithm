x=[]
y=[]
for _ in range(3):
    m, n = map(int,input().split())
    x.append(m)
    y.append(n)
xs = list(set(x))
ys = list(set(y))

if x.count(xs[0])==1:
    print(xs[0],end=" ")
else:
    print(xs[1],end=" ")
if y.count(ys[0])==1:
    print(ys[0])
else:
    print(ys[1])