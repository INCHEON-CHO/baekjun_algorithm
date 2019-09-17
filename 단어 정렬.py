import sys

N = int(sys.stdin.readline())

arr = set([])
for _ in range(N):
    arr.add(input())
arr = list(arr)
arr = sorted(arr, key=lambda x:(len(x),x))
for i in range(len(arr)):
    print(arr[i])