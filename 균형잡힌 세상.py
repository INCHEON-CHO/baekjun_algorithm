line = input()

while line!='.':
    b=0
    stack = []
    for i in range(len(line)):
        if line[i]=='(':
            stack.append('(')
        if line[i]=='[':
            stack.append('[')
        if line[i]==')':
            if len(stack)==0 or stack[-1]=='[':
                b=1
                break
            else:
                stack.pop()
        if line[i]==']':
            if len(stack)==0 or stack[-1]=='(':
                b=1
                break
            else:
                stack.pop()
    if b==1 or len(stack)!=0:
        print('no')
    else:
        print('yes')
    line = input()