N=int(input())
list4=[]

for _ in range(N):
    list2= list(map(str, input().split()))
    a=int(list2[0])
    b= ""
    list3=[]
    for i in list2[1]:
        c = str(i)
        b += c*a
        list3.append(b)
    list4.append(list3[-1])


for j in list4:
    print(j)

