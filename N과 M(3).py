N, M = map(int, input().split())

arr = [0]*M

def go(idx, n, m):
    if idx==m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
    else:
        for i in range(1,n+1):
            arr[idx]=i
            go(idx+1,n,m)

go(0,N,M)