n = int(input())

array=[]
for i in range(n):
    a,b= map(int,input().split())
    array.append([a,b])
array.sort()
array.sort(key=lambda x:x[1])
for i in range(n):
    print(*array[i])