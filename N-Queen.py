import sys

N = int(sys.stdin.readline())

col = [-1]*N

def promising(i, col):
    k = 0
    switch = True

    while k<i and switch:
        if col[i]==col[k] or abs(col[i]-col[k])==i-k:
            switch = False
            break
        k+=1
    return switch

cnt = 0
def queens(i,n,col):
    global cnt
    if promising(i,col):
        if i==n-1:
            cnt+=1
        else:
            for j in range(n):
                col[i+1]=j
                queens(i+1,n,col)

queens(-1,N,col)

print(cnt)