x,y,w,h = map(int, input().split())
l = [x,w-x,y,h-y]
print(min(l))
