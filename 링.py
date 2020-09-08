def GCD(a, b):
    while b:
        a, b = b, a%b
    return a
N = int(input())
ring_list = list(map(int, input().split()))

for i in range(1,N):
    gcd = GCD(ring_list[0], ring_list[i])
    print(ring_list[0]//gcd,'/',ring_list[i]//gcd,sep='')
    