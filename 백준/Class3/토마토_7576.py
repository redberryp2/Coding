# 2차원 BFS

from collections import deque

def BFS(tomato, N, M):
    # 네 방향(상하좌우) 정의
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()

    # 초기 익은 토마토 위치를 큐에 추가
    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 1:
                queue.append((n, m, 0))  # (x, y, days)

    max_days = 0

    # BFS 시작
    while queue:
        x, y, days = queue.popleft()
        max_days = max(days, max_days)  # 최대 날짜 갱신

        # 네 방향 탐색
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            # 범위 내에 있으며 익지 않은 토마토인 경우
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1  # 토마토 익음 처리
                queue.append((nx, ny, days + 1))

    # 익지 못한 토마토가 있는지 확인
    for row in tomato:
        if 0 in row:  # 익지 않은 토마토가 남아있는 경우
            return -1

    return max_days  # 모든 토마토가 익었을 때 걸린 일수

def main():
    M, N = map(int, input().split())  # 행과 열의 개수를 입력받음
    tomato = []
    for _ in range(N):
        tomato.append(list(map(int, input().split())))

    result = BFS(tomato, N, M)
    print(result)

if __name__ == "__main__":
    main()
