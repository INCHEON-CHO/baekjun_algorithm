N = int(input())

binaryList = [0]*1000000
binaryList[0]=1
binaryList[1]=2
for i in range(2,1000000):
    binaryList[i]=(binaryList[i-1]+binaryList[i-2])%15746

print(binaryList[N-1])
