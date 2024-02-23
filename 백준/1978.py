import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

count=0

for i in a:
    if i ==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j ==0:
            break
    else:
        count+=1
print(count)
