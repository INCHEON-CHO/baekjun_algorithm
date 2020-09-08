input()
f_list = list(map(int, input().split()))
f_list.sort()

print(f_list[0]*f_list[-1])