n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]
sum = 0

for i in range(n-1, -1, -1):
    if coin[i] <= k:
        sum += k // coin[i]  # 현재 동전으로 만들 수 있는 최대 개수
        k %= coin[i]  # 남은 금액 업데이트

print(sum)
