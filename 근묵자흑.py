'''n, k = map(int, input().split())

input()

n -= k # n = n - k
mod = n // (k-1)
r = 1 if n % (k-1) else 0
answer = mod + r + 1
print(answer)
'''

a=input()
b=input()
A=int(a)
for i in range(3):
    print(A*int(b[-i+2]))
B=int(b)
print(A*B)
