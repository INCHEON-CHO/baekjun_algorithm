import math

m,n = map(int,input().split())
l = [2]
s = 2
if m<=2:
    print(2)
while (s<=n):
    b=0
    for k in l:
        if s%k==0:
            b=1
            break
        if k>int(math.sqrt(s)):
            break
    if b==0:
        l.append(s)
        if s>=m:
            print(s)
    s+=1
