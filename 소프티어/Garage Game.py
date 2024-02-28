from collections import deque

dx = [0, 1, 0, -1]   # 위 오른쪽 아래 왼쪽 순의 dx,dy update
dy = [-1, 0, 1, 0]

class Info:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def get_coordinates(self):
        return self.y, self.x

def dfs(cnt, total_sum):
    global answer
    check = [[False] * 15 for _ in range(15)]
    dup = [row[:] for row in arr]

    for i in range(2*num, 3*num):
        for j in range(num):
            val = dup[i][j]
            if val == 0 or check[i-2*num][j]:
                continue

            arr[:] = [row[:] for row in dup]
            minX, maxX, minY, maxY = j, j, i, i
            queue = deque()
            same = 1
            queue.append(Info(i, j))
            check[i-2*num][j] = True

            while queue:
                info = queue.popleft()
                cy, cx = info.get_coordinates()
                arr[cy][cx] = 0
                minX = min(minX, cx)
                maxX = max(maxX, cx)
                minY = min(minY, cy)
                maxY = max(maxY, cy)

                for k in range(4):
                    nx, ny = cx + dx[k], cy + dy[k]
                    if 0 <= nx < num and 2*num <= ny < 3*num and not check[ny-2*num][nx] and dup[ny][nx] == val:
                        check[ny-2*num][nx] = True
                        queue.append(Info(ny, nx))
                        same += 1

            if cnt < 2:
                for k in range(minX, maxX+1):
                    for m in range(maxY, minY-1, -1):
                        if arr[m][k] != 0:
                            continue
                        jump = 0
                        for l in range(m-1, -1, -1):
                            if arr[l][k]:
                                jump = m - l
                                break
                        if jump:
                            for l in range(m, jump-1, -1):
                                arr[l][k] = arr[l-jump][k]
                                arr[l-jump][k] = 0
                dfs(cnt + 1, total_sum + same + (maxX - minX + 1) * (maxY - minY + 1))
            else:
                answer = max(answer, total_sum + same + (maxX - minX + 1) * (maxY - minY + 1))

if __name__ == "__main__":
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(3*num)]
    answer = 0
    dfs(0, 0)
    print(answer)
