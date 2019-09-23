import sys
n = int(sys.stdin.readline())
stack = []
ans = ''
idx = 1
b = 0
for i in range(n):
    item = int(sys.stdin.readline())
    if idx<=item:
        while(idx<=item):
            stack.append(idx)
            ans+='+'
            idx+=1
    if stack[-1]==item:
        stack.pop()
        ans+='-'
    else:
        b=1
if b==0:
    for i in ans:
        print(i)
else:
    print('NO')