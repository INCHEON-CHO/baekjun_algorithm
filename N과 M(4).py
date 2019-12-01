N, M = map(int, input().split())

arr = [0]*(M+1)

def go(idx, n, m):
    if idx==m+1:
        for i in range(1,m+1):
            print(arr[i],end=" ")
        print()
    else:
        for i in range(1,n+1):
            if arr[idx-1]>i:
                continue
            arr[idx]=i
            go(idx+1,n,m)

go(1,N,M)