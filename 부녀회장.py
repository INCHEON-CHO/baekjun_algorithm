T = int(input())
mat = [[0]*15 for i in range(15)]
for i in range(1,15):
    mat[0][i]=i
for i in range(1,15):
    for j in range(1,15):
        mat[i][j] = mat[i-1][j] + mat[i][j-1]
for i in range(T):
    k = int(input())
    n = int(input())
    print(mat[k][n])