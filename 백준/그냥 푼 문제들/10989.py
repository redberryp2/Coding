import sys

n=int(sys.stdin.readline())
list1=[0] * 10001
for _ in range(n):
    list1[int(sys.stdin.readline())] += 1

for i in range(10001):
    if list1[i] != 0:
        for j in range(list1[i]):
            print(i)
