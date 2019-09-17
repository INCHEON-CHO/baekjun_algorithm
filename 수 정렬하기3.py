import sys
N = int(sys.stdin.readline())

arr = [0]*10000

for i in range(N):
    arr[int(sys.stdin.readline())-1]+=1
for i in range(10000):
    print((str(i+1)+'\n')*arr[i],sep="",end="")
