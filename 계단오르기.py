T = int(input())
stairs = [0]*(T+1)
for i in range(1,T+1):
    stairs[i] = int(input())
D = [0]*(T+1)
D[1]=stairs[1]
D[2]=stairs[2]+stairs[1]
for i in range(3,T+1):
    D[i]=max(stairs[i]+stairs[i-1]+D[i-3],stairs[i]+D[i-2])

print(D[-1])
'''
recursive
def upStairs(start, prev):
    if start>T:
        return -3000000
    elif start==T:
        return stairs[-1]
    elif prev==0:
        return stairs[start]+max(upStairs(start+1,1),upStairs(start+2,0))
    elif prev==1:
        return stairs[start]+upStairs(start+2,0)
print(max(upStairs(1,0),upStairs(2,0)))'''
