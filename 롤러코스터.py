r, c = map(int,input().split())
mat = []
for i in range(r):
    mat.append(input().split())
s = ""
if (r%2==1):
    for i in range(r):
        if i!=r-1:
            if i%2==0:
                s+='R'*(c-1)
                s+='D'
            else:
                s+='L'*(c-1)
                s+='D'
        else:
            s+='R'*(c-1)
elif (c%2==1):
    for i in range(c):
        if i!=c-1:
            if i%2==0:
                s+='D'*(r-1)
                s+='R'
            else:
                s+='U'*(r-1)
                s+='R'
        else:
            s+='D'*(r-1)
else:
    x=0
    y=1
    for i in range(r):
        for j in range(c):
            mat[i][j] = int(mat[i][j])
            if (i+j)%2==1:
                if mat[x][y]>mat[i][j]:
                    x=i
                    y=j
    x1=0
    y1=0
    x2=r-1
    y2=c-1
    s2=""
    while x2-x1>1:
        if x1//2<x//2:
            s+='R'*(c-1)
            s+='D'
            s+='L'*(c-1)
            s+='D'
            x1+=2
        if x//2<x2//2:
            s2+='D'
            s2+='L'*(c-1)
            s2+='D'
            s2+='R'*(c-1)
            x2-=2
    while y2-y1>1:
        if y1//2<y//2:
            s+='DRUR'
            y1+=2
        if y//2<y2//2:
            s2='RURD'+s2
            y2-=2
    if y==y1:
        s+='RD'
    else:
        s+='DR'
    s+=s2

print(s)