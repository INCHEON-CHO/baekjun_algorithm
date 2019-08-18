A,B,V = map(int,input().split())

distance=(V-A)//(A-B)+1
if (V-A)%(A-B)!=0:
    distance+=1
print(distance)
