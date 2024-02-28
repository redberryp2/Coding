import sys

n, m = map(int, sys.stdin.readline().split())

list1 = [sys.stdin.readline().strip() for _ in range(n)]
list2 = [sys.stdin.readline().strip() for _ in range(m)]

hash_map = {}
for item in list1:
    key, value = item.split(' ', 1)  # ù ��° ������ �������� Ű�� ���� �и�
    hash_map[key] = value

for query in list2:
    if query in hash_map:
        print(hash_map[query])
