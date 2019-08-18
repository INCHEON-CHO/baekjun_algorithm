T = int(input())

for i in range(T):
    H,W,N = map(int, input().split())
    su = (N-1)%H+1
    nu = (N-1)//H+1
    if nu>=10:
        print(su,nu,sep="")
    else:
        print(su,0,nu,sep="")