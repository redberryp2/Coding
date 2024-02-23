from collections import deque


def BFS(x,y):
    dx=[-1,-1,0,0]
    dy=[0,0,-1,-1]
    queue=deque()
    queue.append((x,y))
    info[x][y]=board[x][y]
    while queue:
        X, Y= queue.popleft()
        for i in range(4):
            NEW_X= X + dx[i]
            NEW_Y= Y + dy[i]
            if 0 <= NEW_X < N and 0 <= NEW_Y < N:
                if info[NEW_X][NEW_Y] > board[NEW_X][NEW_Y] + info[X][Y]:
                    info[NEW_X][NEW_Y] =board[NEW_X][NEW_Y] + info[X][Y]
                    queue.append((NEW_X,NEW_Y))


N=1
tc=0
while N != 0:
    N = int(input())
    if N ==0:
        break
    board = deque([list(map(int,input().split())) for _ in range(N)])
    info = deque([[1e9]*N for _ in range(N)])
    BFS(0,0)
    tc+=1
    print(tc,info[N-1][N-1])