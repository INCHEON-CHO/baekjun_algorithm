import sys

N = int(sys.stdin.readline())

arr = [0]*N
arr1 = [0]*8001
s = 0
m = 0
for i in range(N):
    item = int(sys.stdin.readline())
    arr[i] = item
    s+=arr[i]
    arr1[item+4000]+=1
    if m<arr1[item+4000]:
        m = arr1[item+4000]
    
arr.sort()
i_list = []
for i in range(8001):
    if m==arr1[i]:
        i_list.append(i-4000)
    if len(i_list)==2:
        break
print(int(round(s/N,0)))
print(arr[N//2])
print(i_list[-1])
print(arr[-1]-arr[0])

