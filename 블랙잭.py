n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
here=0
bvalue=0
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            here=cards[i]+cards[j]+cards[k]
            if here==m:
                ans=here
                bvalue=1
                break
            if here>ans and here<m:
                ans=here
        if bvalue==1:
            break
    if bvalue==1:
        break
print(ans)