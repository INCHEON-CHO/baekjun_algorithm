import math
l=[2]
for i in range(3,10000):
    b=0
    for k in l:
        if i%k==0:
            b=1
            break
        if k>math.sqrt(i):
            break
    if b==0:
        l.append(i)
for _ in range(int(input())):
    n = int(input())
    resultA, resultB = 0,0
 
    pre, idx = 0,0
    for i in range(len(l)):
        if l[i] <= n/2 and l[i] > pre:
            pre = l[i]
            idx = i
        else:
            break
 
    while True:
        b = 0
        for i in range(idx, len(l)):
            if pre + l[i] == n:
                resultA = pre
                resultB = l[i]
                b = 1
                break
        if b == 1:
            break
        else:
            idx -= 1
            pre = l[idx]
    print(resultA, resultB)