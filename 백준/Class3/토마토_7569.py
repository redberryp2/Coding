# 3차원 그래프 문제

from collections import deque

def bfs(tomato, M, N, H):	# 6방향 Direction 설정 및 전형적인 BFS 실행 X, Y ,Z와 날짜를 한묶음으로 본다. 
	directions = [(1, 0, 0), (-1 ,0, 0), (0, 1, 0), (0 , -1, 0), (0, 0 ,1), (0, 0, -1)]
	queue = deque()

	for h in range(H):
		for n in range(N):
			for m in range(M):
				if tomato[h][n][m] == 1:
					queue.append((h, n, m, 0)) 

	max_days = 0

	while queue:
		z, y, x , days = queue.popleft()
		max_days = max(days, max_days)

		for dz, dy, dx in directions:
			nz, ny, nx = z + dz, y + dy, x + dx
			if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0:  # 해제 조건 
				tomato[nz][ny][nx] = 1
				queue.append((nz, ny, nx, days+1))

	for h in range(H):
		for n in range(N):
			for m in range(M):
				if tomato[h][n][m] == 0:
					return -1
	return max_days

def main():   # 입력 데이터를 3차원으로 만들어 주기
	M, N, H = map(int, input().split())
	tomato = []
	for _ in range(H):
		box = []
		for _ in range(N):
			box.append(list(map(int,input().split())))
		tomato.append(box)
	result = bfs(tomato, M, N, H)
	print(result)

if __name__ == "__main__":
	main()

# from collections import deque

# def bfs(tomato, H, M, N):
# 	direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0 ,1), (0 , 0, -1)]
# 	queue = deque()
# 	for h in range(H):
# 		for m in range(M):
# 			for n in range(N):
# 				if tomato[h][m][n] == 1:
# 					queue.append((h, m, n, 0))
	
# 	max_days = 0

# 	while queue:
# 		z, y, x, days = queue.popleft()
# 		max_days = max(days, max_days)
		
# 		for dz, dy, dx in direction:
# 			nz, ny, nx = z + dz, y + dy, x + dx
# 			if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N and tomato[nz][ny][nx] ==0:
# 				tomato[nz][ny][nx] = 1
# 				queue.append((nz, ny, nx, days + 1))

# 	for h in range(H):
# 		for m in range(M):
# 			for n in range(N):
# 				if tomato[h][m][n] == 0:
# 					return -1
# 	return max_days

# def main():
#     H, M, N = map(int, input().split())
#     tomato = []
#     for h in range(H):
#         tmp = []
#         for m in range(M):
#             tmp.append(list(map(int, input().split())))
#         tomato.append(tmp)
#     result = bfs(tomato, H, M ,N)
#     print(result)
        
# if __name__ =="__main__":
#     main()