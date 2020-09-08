n = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))


MIN = 1000000000
MAX = -1000000000

def go(elem, idx, op_list):
    global MIN, MAX
    if idx==n:
        if elem<MIN:
            MIN = elem
        if elem>MAX:
            MAX = elem
    else:
        for j in range(4):
            if op_list[j]!=0:
                op_list[j]-=1
                if j==0:
                    go(elem+A[idx], idx+1, op_list)
                elif j==1:
                    go(elem-A[idx], idx+1, op_list)
                elif j==2:
                    go(elem*A[idx], idx+1, op_list)
                else:
                    if elem<0:
                        go(-((-elem)//A[idx]), idx+1, op_list)
                    else:
                        go(elem//A[idx], idx+1, op_list)
                
                op_list[j]+=1

go(A[0], 1, oper)
print(MAX, MIN)