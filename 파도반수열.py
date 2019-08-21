T = int(input())

TriangleList = [0]*100
TriangleList[0]=1
TriangleList[1]=1
TriangleList[2]=1

for i in range(3,100):
    TriangleList[i]=TriangleList[i-2]+TriangleList[i-3]

for _ in range(T):
    N = int(input())
    print(TriangleList[N-1])