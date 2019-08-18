l=[0]*3
l[0], l[1], l[2] = map(int, input().split())
l.sort()
while (sum(l)!=0):
    if l[0]**2+l[1]**2==l[2]**2:
        print('right')
    else:
        print('wrong')
    l=[0]*3
    l[0], l[1], l[2] = map(int, input().split())
    l.sort()