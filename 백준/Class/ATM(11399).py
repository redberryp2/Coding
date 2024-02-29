import sys
N = int(sys.stdin.readline())

list1 =list(map(int,input().split()))

list1 = sorted(list1)
sum1 = 0
for i in range(N):
    sum1 += sum(list1[:i+1])
print(sum1)