N = int(input())
m = N//5
if N==4 or N==7:
    print(-1)
else:
    for i in range(m):
        if (m*5==N):
            print(m)
            break;
        elif ((N-m*5)%3==0):
            print(m+(N-m*5)//3)
            break;
        else:
            m=m-1
    if (m==0):
        print(N//3)