N = int(input())
arr = []
for i in range(N):
    l = list(input().split())
    l[0] = int(l[0])
    l.append(i)
    arr.append(l)
arr = sorted(arr, key=lambda x:(x[0],x[2]))
for i in range(N):
    print(arr[i][0],arr[i][1])
