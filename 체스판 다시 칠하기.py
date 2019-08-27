n, m = map(int, input().split())
pad = []
for i in range(n):
    line = input()
    pad.append(line)

boards = [['WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'],
    ['BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB']]
ans = 64
for x in range(n-7):
    for y in range(m-7):
        for i in range(2):
            cnt=0
            for j in range(8):
                for k in range(8):
                    cnt+=(boards[i][j][k]!=pad[x+j][y+k])
            ans = min(cnt,ans)
print(ans)