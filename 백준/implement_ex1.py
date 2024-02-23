# #상하좌우 구현문제
# import sys
#
# n=int(sys.stdin.readline()) #the scale of matrix
# f_matrix=[[[i,j] for j in range(n) ] for i in range(5)]
# print(f_matrix)
# array_list=[sys.stdin.readline().split()]
# print(array_list)
# result=[0,0]
# for x in array_list:
#     if x == 'L':
#         result-[0,1]
#         if 0 > (result[0] and result[1]) >5:
#             continue
#     if x == 'R':
#         result+[0,1]
#         if 0 > (result[0] and result[1]) >5:
#             continue
#     if x == 'U':
#         result-[1,0]
#         if 0 > (result[0] and result[1]) >5:
#             continue
#     if x == 'D':
#         result+[1,0]
#         if 0 > (result[0] and result[1]) >5:
#             continue
# print(result)
import sys

#n
n=int(sys.stdin.readline())

x,y=1,1
plans= sys.stdin.readline().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['L','R','U','D']
 
for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue
    x,y =nx, ny
print(nx,ny)


