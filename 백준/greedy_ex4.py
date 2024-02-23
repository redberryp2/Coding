#1이 될때까지
import sys

n,m = map(int,sys.stdin.readline().split())
result=0

while n >= m:  # 나누기가 많아질 때 최적의 수가 보장
    while n % m != 0:
        n -= 1
        result += 1
    n= n // m
    result +=1

while n > 1:
    n -= 1
    result +=1

print(result)


