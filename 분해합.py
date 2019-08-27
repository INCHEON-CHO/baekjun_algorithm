n = int(input())
bvalue=0
for i in range(1,n+1):
    ans=i
    for j in str(i):
        ans+=int(j)
    if ans==n:
        print(i)
        bvalue=1
        break
if bvalue==0:
    print(0)