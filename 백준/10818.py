n=int(input())

list1=list(map(int,input().split()))
list2=[]
list2.append(min(list1))
list2.append(max(list1))

print(*list2)