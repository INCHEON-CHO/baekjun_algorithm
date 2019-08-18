N = int(input())

cnt = 1
first=2
if N==1:
    print(cnt)
else:
    while(1):
        if(first<=N and first+6*cnt>N):
            print(cnt+1)
            break;
        else:
            first+=6*cnt
            cnt+=1
