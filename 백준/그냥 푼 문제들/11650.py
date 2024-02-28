n = int(input())
x_list=[]
for i in range(n):
    x_list.append(list(map(int,input().split())))
x_list.sort(key=lambda x:x[1])
x_list.sort()
for i in range(n):
    print(*x_list[i])
