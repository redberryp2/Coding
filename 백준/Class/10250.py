n=int(input())
result=[]
for _ in range(n):
    a, b, c= map(int,input().split())
    if c % a == 0:
        x = a * 100
        y = (c // a)
    else:
        x = (c % a) * 100
        y = (c // a + 1)

    result.append(x + y)


print(*result,sep='\n')