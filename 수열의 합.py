n, m = map(int,input().split())
first=0
length=0
b=0
for i in range(m,101):
    if (n*2)/i-i+1<0:
        break
    if ((n*2)/i-i+1)%2==0:
        first = int(((n*2)/i-i+1)//2)
        length = i
        b=1
        break
if b==0:
    print(-1)
else:
    for i in range(length):
        print(first+i,end=" ")