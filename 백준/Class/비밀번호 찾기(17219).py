import sys

n, m = map(int, sys.stdin.readline().split())

list1 = [sys.stdin.readline().strip() for _ in range(n)]
list2 = [sys.stdin.readline().strip() for _ in range(m)]

hash_map = {}
for item in list1:
    key, value = item.split(' ', 1)  # 첫 번째 공백을 기준으로 키와 값을 분리
    hash_map[key] = value

for query in list2:
    if query in hash_map:
        print(hash_map[query])
