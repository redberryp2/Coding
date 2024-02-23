#DFS 너비우선탐색
#큐 사용
#큐에 시작 숫자넣고 시작숫자에 간선 연결된 숫자들 전부
# 그다음

from collections import deque

n,m,v = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(m)]

def BFS(graph,start):
    queue=deque(start)
    visited=[]
    while queue:
        current=queue.popleft()  #데크 왼쪽값 저장
        for i in graph[current-1]:
            visited.append(current)
            if not visited:
                queue.append(i)

    return visited

print(BFS(graph,v))








