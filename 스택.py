import sys
N = int(sys.stdin.readline())
stack = []
length = 0
for i in range(N):
    l = list(sys.stdin.readline().split())
    if l[0]=='push':
        stack.append(l[1])
        length+=1
    elif l[0]=='pop':
        if length>0:
            print(stack.pop())
            length-=1
        else:
            print(-1)
    elif l[0]=='size':
        print(length)
    elif l[0]=='empty':
        print(int(length==0))
    else:
        if length==0:
            print(-1)
        else:
            print(stack[-1])
