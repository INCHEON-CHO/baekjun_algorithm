l = list(input())
if '0' not in l:
    print(-1)
else:
    s = 0
    for i in range(len(l)):
        s+=int(l[i])
    l.sort(reverse=True)
    if s%3==0:
        print("".join(l))
    else:
        print(-1)

