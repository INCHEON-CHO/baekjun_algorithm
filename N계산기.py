n = int(input)
answer = ""
if n%2==0:
    answer+='1'*(n//2)
else:
    answer+=('7'+'1'*((n-3)//2))