import sys
from copy import deepcopy

n= int(sys.stdin.readline())
result2=[]
for x in range(n):
    a= list(map(int,sys.stdin.readline().split()))
    b= list(map(int,sys.stdin.readline().split()))

    result=0
    list_array=[]
    second=[[0,0] for i in range(len(b))]
    for j in range(len(b),1,-1):
        for k in range(len(a),1,-1):
            if b[j-1] ==a[k-1]:
                list_array.append([j-1,k-1])

    list_array2=deepcopy(list_array)
    list_array2.sort(key=lambda x: x[1],reverse=True)
    for t in range(len(b)-1):
        if list_array[t]==list_array2[t]:
            result +=1
        else:
            del (list_array[t])
            list_array.insert(t,[0,0])
            if list_array[t] == list_array2[t]:
                result +=1
    result2.append(result)

print(*result2)




# 1 2 3 4 5 6 7
# 1 2 3 4 5
#
# (5,7),(4,6),(3,1),(2,4),(1,3)
# sort(lamda=x,x[1])
# (5,7),(4,6),(2,4),(1,3),(3,1)
# #스택 만들어서 같은 인덱스 +1 다르면 위에 리스트 삭제!


















