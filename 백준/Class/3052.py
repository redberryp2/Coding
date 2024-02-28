list1=[]
for _ in range(10):
    n= int(input())
    list1.append(n)
list2=[]
for i in list1:
    b=i % 42
    list2.append(b)

print(len(set(list2)))


