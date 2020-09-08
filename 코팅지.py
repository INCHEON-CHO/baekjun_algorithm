n = int(input())
for _ in range(n):
    h, w = map(int, input().split())
    mat = []
    find = [[0]*w for i in range(h)]
    for i in range(h):
        mat.append(list(map(int, input().split())))
    for i in range(h-1):
        for j in range(w-1):
            if mat[i][j] and mat[i][j+1] and mat[i+1][j] and mat[i+1][j+1]:
                find[i][j]=1
                find[i][j+1]=1
                find[i+1][j]=1
                find[i+1][j+1]=1
    if find == mat:
        print("YES")
    else:
        print("NO")
