a = int(input())
b = int(input())
c = int(input())
cnt=[]

d = str(a * b * c)
list=["0","1","2","3","4","5","6","7","8","9"]

for j in list:
    count= d.count(j)
    cnt.append(count)

for i in range(10):
    print(cnt[i])