import math

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
            continue
    dist = (x2-x1)**2+(y2-y1)**2
    add = (r1+r2)**2
    sub = (r1-r2)**2
    if dist>sum:
        print(0)
    elif dist==sum:
        print(1)
    else:
        if dist==sub:
            print(1)
        elif dist<sub:
            print(0)
        else:
            print(2)