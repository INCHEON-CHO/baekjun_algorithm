import math

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
num_list.sort()

gcd = num_list[1] - num_list[0]
for i in range(1, n-1):
    gcd = GCD(gcd, num_list[i+1]-num_list[i])

res = []
limit = int(math.sqrt(gcd))
for i in range(1, limit+1):
    if gcd%i==0:
        res.append(i)
        if gcd//i!=i:
            res.append(gcd//i)
res.sort()
for i in range(1,len(res)):
    print(res[i], end=' ')