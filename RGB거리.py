N = int(input())
allList = []
for i in range(N):
    row = list(map(int,input().split()))
    allList.append(row)
for i in range(1,N):
    allList[i][0]+=min(allList[i-1][1],allList[i-1][2])
    allList[i][1]+=min(allList[i-1][0],allList[i-1][2])
    allList[i][2]+=min(allList[i-1][0],allList[i-1][1])

print(min(allList[-1]))