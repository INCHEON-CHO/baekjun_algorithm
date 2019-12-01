n = int(input())
mat = [[' ']*n for _ in range(n)]

def star(n, x, y):
    if n==3:
        mat[x][y] = "*"
        mat[x+1][y] = "*"
        mat[x+2][y] = "*"
        mat[x][y+1] = "*"
        mat[x+2][y+1] = "*"
        mat[x][y+2] = "*"
        mat[x+1][y+2] = "*"
        mat[x+2][y+2] = "*"
    else:
        m = n//3
        star(m,x,y)
        star(m,x+m,y)
        star(m,x+2*m,y)
        star(m,x,y+m)
        star(m,x+2*m,y+m)
        star(m,x,y+2*m)
        star(m,x+m,y+2*m)
        star(m,x+2*m,y+2*m)
star(n,0,0)

for i in range(n):
    for j in range(n):
        print(mat[i][j],end="")
    print()