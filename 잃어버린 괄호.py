s = input()
s = s.split('-')
for i in range(len(s)):
    s[i] = s[i].split('+')
ans = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        if i==0:
            ans+=int(s[i][j])
        else:
            ans-=int(s[i][j])
print(ans)