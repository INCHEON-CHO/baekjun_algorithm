N, M = map(int,input().split())

check = [0]*(N+1)
arr = [0]*M

def go(idx, n, m):
    if idx == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()
    else:
        for i in range(1, n+1):
            if check[i]:
                continue
            check[i]=1
            arr[idx]=i
            go(idx+1, n, m)
            check[i] = 0
go(0, N, M)