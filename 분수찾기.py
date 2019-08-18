N = int(input())

first=1
cnt=1

while(1):
    if first<=N and first+cnt>N:
        if cnt%2==0:
            print(1+(N-first),'/',cnt-N+first,sep="")
            break;
        else:
            print(cnt-N+first,'/',1+(N-first),sep="")
            break;
    else:
        first+=cnt
        cnt+=1