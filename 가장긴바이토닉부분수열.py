N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(reversed(arr1))

D1 = [0]*(N+1)
D2 = [0]*(N+1)

for i in range(1,N+1):
    cnt1=0
    cnt2=0
    for j in range(1,i):
        if arr1[i-1]>arr1[j-1]:
            cnt1 = max(cnt1,D1[j])
        if arr2[i-1]>arr2[j-1]:
            cnt2 = max(cnt2,D2[j])
    D1[i]=cnt1+1
    D2[i]=cnt2+1
ans=0
for i in range(1,N+1):
    ans = max(ans, D1[i]+D2[N+1-i])
print(ans-1)