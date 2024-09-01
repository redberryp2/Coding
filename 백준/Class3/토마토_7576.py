# 2���� BFS

from collections import deque

def BFS(tomato, N, M):
    # �� ����(�����¿�) ����
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()

    # �ʱ� ���� �丶�� ��ġ�� ť�� �߰�
    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 1:
                queue.append((n, m, 0))  # (x, y, days)

    max_days = 0

    # BFS ����
    while queue:
        x, y, days = queue.popleft()
        max_days = max(days, max_days)  # �ִ� ��¥ ����

        # �� ���� Ž��
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            # ���� ���� ������ ���� ���� �丶���� ���
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1  # �丶�� ���� ó��
                queue.append((nx, ny, days + 1))

    # ���� ���� �丶�䰡 �ִ��� Ȯ��
    for row in tomato:
        if 0 in row:  # ���� ���� �丶�䰡 �����ִ� ���
            return -1

    return max_days  # ��� �丶�䰡 �;��� �� �ɸ� �ϼ�

def main():
    M, N = map(int, input().split())  # ��� ���� ������ �Է¹���
    tomato = []
    for _ in range(N):
        tomato.append(list(map(int, input().split())))

    result = BFS(tomato, N, M)
    print(result)

if __name__ == "__main__":
    main()
