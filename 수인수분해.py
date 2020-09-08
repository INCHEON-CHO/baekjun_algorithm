num = int(input())

limit = int(num**0.5)
div = 2
while div <= limit:
    while not num % div:
        num //= div
        print(div)
    div += 1

if num > 1:
    print(num)