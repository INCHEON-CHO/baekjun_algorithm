while 1:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        if a % b == 0:
            print('multiple')
        elif b % a == 0:
            print('factor')
        else:
            print('neither')