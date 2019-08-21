n = int(input())

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    i=0
    f1=1
    f0=0
    while(i<=n-2):
        temp = f1
        f1=f1+f0
        f0=temp
        i+=1
    print(f1)
