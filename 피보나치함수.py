T = int(input())
numList = [[0,0] for _ in range(41)]
numList[0]=[1,0]
numList[1]=[0,1]

for i in range(2,41):
    numList[i][0]=numList[i-1][0]+numList[i-2][0]
    numList[i][1]=numList[i-1][1]+numList[i-2][1]

for _ in range(T):
    fibnum = int(input())
    print(numList[fibnum][0],numList[fibnum][1])