import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
if N==1:
    print(-1)
else:
    arr = [[i,v] for i,v in enumerate(arr)]
    ans = [-1]*N
    stack = [arr[0]]
    idx=1
    while 1:
        if stack and stack[-1][1]<arr[idx][1]:
            ans[stack[-1][0]]=arr[idx][1]
            stack.pop()
        else:
            stack.append(arr[idx])
            idx+=1
            if idx>=N:
                break
    for i in ans:
        print(i,end=" ")