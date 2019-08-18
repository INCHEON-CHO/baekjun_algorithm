T = int(input())
plus = []
minus = []
ones = 0
zeros = 0
for _ in range(T):
    x = int(input())
    if x==1:
        ones+=1
    elif x>0:
        plus.append(x)
    elif x<0:
        minus.append(x)
    else:
        zeros+=1

plus.sort(reverse = True)
minus.sort()

if len(plus)%2==1:
    plus.append(1)
if len(minus)%2==1:
    if zeros>0:
        minus.append(0)
    else:
        minus.append(1)
ans = ones
for i in range(len(plus)//2):
    ans+=(plus[2*i]*plus[2*i+1])
for i in range(len(minus)//2):
    ans+=(minus[2*i]*minus[2*i+1])
print(ans)