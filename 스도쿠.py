grid = [list(map(int,input().split())) for _ in range(9)]

zeroIdx = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            zeroIdx.append([i,j])

def promising(a):

    numList1 = [0]*10
    numList2 = [0]*10
    numList3 = [0]*10
    val1 = a[0]//3
    val2 = a[1]//3
    for i in range(9):
        num1 = grid[a[0]][i]
        num2 = grid[i][a[1]]
        num3 = grid[val1*3+i//3][val2*3+i%3]
        numList1[num1]+=1
        numList2[num2]+=1
        numList3[num3]+=1
        if (numList1[num1]>1 and num1!=0) or (numList2[num2]>1 and num2!=0) or (numList3[num3]>1 and num3!=0):
            return False
    
    return True

flag = False
def DFS(idx):
    global flag

    if flag:
        return
    if idx==len(zeroIdx):
        for i in range(9):
            for j in range(9):
                print(grid[i][j],end=' ')
            print()
        flag=True
        return
    tmpidx = zeroIdx[idx]
    for j in range(1,10):
        grid[tmpidx[0]][tmpidx[1]]=j
        if promising(tmpidx):
            DFS(idx+1)
        #grid[tmpidx[0]][tmpidx[1]]=0

DFS(0)
