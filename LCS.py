line1 = input()
line2 = input()

D = [[0]*1001 for _ in range(1001)]

for i in range(1, len(line1)+1):
    for j in range(1,len(line2)+1):
        if line1[i-1]== line2[j-1]:
            D[i][j]=D[i-1][j-1]+1
        else:
            D[i][j]=max(D[i-1][j],D[i][j-1])
print(D[len(line1)][len(line2)])
