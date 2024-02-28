import sys
n,m = map(int,sys.stdin.readline().split())

a =set()
for i in range(n):
    a.add(input())

b =set()
for i in range(m):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)