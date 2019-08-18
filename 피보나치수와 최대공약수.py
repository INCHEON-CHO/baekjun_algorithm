import math

n, m = map(float, input().split())

def fibo(x):
    a=((1+math.sqrt(5))/2)**x
    b=((1-math.sqrt(5))/2)**x
    c=math.sqrt(5)
    return (a-b)//c
def gcd(x,y):
    while(y!=0):
        tmp = x
        x = y
        y = tmp%y
    return x
print(fibo(gcd(n,m))%1000000007)
