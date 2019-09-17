import sys

N = int(sys.stdin.readline())

arr = [[0,0] for _ in range(N)]
for i in range(N):
    arr[i][0], arr[i][1] = map(int, sys.stdin.readline().split())
arr = sorted(arr, key = lambda x:(x[0],x[1]))
for i in range(N):
    print(arr[i][0],arr[i][1])