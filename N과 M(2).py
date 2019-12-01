N, M = map(int, input().split())

check = [0]*(N+1)
arr = [0]*(M+1)

def go(idx, n ,m):
    if idx==m+1:
        for i in range(1,m+1):
            print(arr[i], end=" ")
        print()
    else:
        for i in range(1,n+1):
            if check[i] or arr[idx-1]>i:
                continue
            else:
                check[i]=1
                arr[idx]=i
                go(idx+1,n,m)
                check[i]=0
go(1,N,M)

            