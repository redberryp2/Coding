n = int(input())
b=[1,1,1] + [0]*97
result=[]
for i in range(3,100):
    b[i] = b[i-2]+b[i-3]
for _ in range(n):
    x=int(input())
    result.append(b[x-1])

print(*result,sep='\n')
