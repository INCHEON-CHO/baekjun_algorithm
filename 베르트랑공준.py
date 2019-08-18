import math

l = [2]
for i in range(3,123456*2+1):
    b=0
    for k in l:
        if i%k==0:
            b=1
            break
        if k>math.sqrt(i):
            break
    if b==0:
        l.append(i)

N = int(input())
while(N!=0):
    cnt=0
    for k in l:
        if k>2*N:
            break
        if k>N:
            cnt+=1
    print(cnt)
    N = int(input())