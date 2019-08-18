def Count_block(x,y):
    sub = y-x
    if sub==1:
        return 1
    elif sub==2:
        return 2
    else:
        blocks=3
        inc=2
        min=2
        max=4
        cnt=0
        while(1):
            if min<sub and max>=sub:
                return blocks
            min=max
            max+=inc
            if cnt%2==0:
                inc+=1
            cnt+=1
            blocks+=1

length = int(input())
for i in range(length):
    l = input().split()
    print(Count_block(int(l[0]),int(l[1])))