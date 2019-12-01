N = int(input())

print(2**N-1)

def hanoi(n, start, mid, end):
    if n==1:
        print(start, end)
    else:
        hanoi(n-1, start, end, mid)
        print(start, end)
        hanoi(n-1, mid, start, end)

hanoi(N,1,2,3)