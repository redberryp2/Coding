# import sys
#
# _ = sys.stdin.readline()
# n = sorted(map(int,sys.stdin.readline().split()))
# _ = sys.stdin.readline()
# m = map(int,sys.stdin.readline().split())
#
# def binary(num, n, start ,end):
#     if start > end :
#         return 0
#     middle = (start + end) // 2
#     if n[middle] == num:
#         return n[start:end+1].count(num)
#     elif n[middle] > num:
#         return binary(num, n, start,middle-1)
#     else:
#         return binary(num, n,middle+1,end)
#
# dict_1 ={}
# for i in n:
#     start = 0
#     end = len(n)-1
#     if i not in dict_1:
#         dict_1[i] = binary(i , n , start,end)
#
# print(' '.join(str(dict_1[x]) if x in dict_1 else '0' for x in m ))
# dict_1= {
#     1 : 3,
#     2 : 4,
#     3 : 5
#
# }
# print(" ".join(str(dict_1[i]) for i in range(1,4)))

from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(hashmap)