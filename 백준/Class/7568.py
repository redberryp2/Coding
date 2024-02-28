n= int(input())

list1=[]
for i in range(n):
    a,b = map(int,input().split())
    list1.append([a,b])

result=[]
for j in list1:
    rank=0
    for k in list1:
        if (j[0] <= k[0]) and (j[1] <= k[1]):
            rank += 1
    result.append(rank)

print(*result)

