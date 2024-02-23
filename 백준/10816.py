#1 내가 풀었던 방식
import time
start = time.time()
# n=int(input())
# list1=list(map(int,input().split()))
# m=int(input())
# list2=list(map(int,input().split()))
# bin_list=[]
#
# for i in list2:
#     bin_list.append(list1.count(i))
# end=time.time()
# print(*bin_list)
from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)
print(n_dic)
print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))

#메모리가 상당히 큰거같다.

