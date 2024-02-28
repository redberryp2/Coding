# #12345 각 숫자 더하기
# # sum=0
# # s = input()
# # for i in range(len(s)):
# #     sum += int(s[i])
# #
# # print(sum)
#
# #띄어쓰기 없이 정수 여러개 입력받아 2차원 배열로 저장하기
# # two_d= [list(map(int,input())) for _ in range(4)]
# # print(two_d)
#
# # t_d = [list(map(int, input().split())) for _ in range(3)]
# # print(t_d)
# result=[]
#
# while True:
#     n,m=map(int,input().split())
#     if n == 0 and m == 0:
#         break
#     sea_land= [list(map(int,input().split())) for _ in range(m)]
#
#
#
#
#     sea_land=

graph_list={
    0 : set([1,3]),
    1 : set([0,2,3]),
    2 : set([1,3,4,5]),
    3 : set([0,1,2,4,5]),
    4 : set([2,3]),
    5 : set([2,3,6,7]),
    6 : set([5,8]),
    7 : set([5,8]),
    8 : set([6,7])
}

from collections import deque

def BFS(graph, root):
    visited = []
    #값을 저장할 변수나 자료형 여기서 선언할 것
    queue = deque([root])

    while queue:
    #1. 큐에서 처리할 노드 가져오기
        curent = queue.popleft()
        #2. 해당 노드가 방문 되었었는지 확인할 것
        if curent not in visited:
            #3. 방문했다고 기록
            visited.append(curent)
            queue += graph[curent] - set(visited)
            # 여기서 방문된 상태
            #필요한 처리를 해주세요 current노드를 가지고 필요한 처리 진행

    return visited

def DFS(graph,root):
    visited = []
    stack = [root]

    while stack:
        current =stack.pop()
        if current not  in visited:
            visited.append(current)
            stack += graph[current] - set(visited)
    return visited




print(BFS(graph_list,0))
print(DFS(graph_list,0))









