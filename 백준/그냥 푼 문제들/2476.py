#주사위 게임
import sys

n=int(sys.stdin.readline())
count=[]

for _ in range(n):
    x,y,z=map(int,sys.stdin.readline().split())
    if x==y:
        if y==z:
            count.append(10000+1000*x)
        else:
            count.append(1000+100*x)
    elif x==z:
        count.append(1000+100*x)
    elif y==z:
        count.append(1000+100*y)
    else:
        count.append(max(x,y,z)*100)

print(max(count))


