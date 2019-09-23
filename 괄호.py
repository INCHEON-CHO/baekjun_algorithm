T = int(input())

for i in range(T):
    arr = list(input())
    s = 0
    for j in range(len(arr)):
        if arr[j]=='(':
            s+=1
        else:
            s-=1
        if s<0:
            break
    if s==0:
        print('YES')
    else:
        print('NO')