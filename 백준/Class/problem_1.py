import sys

T = int(sys.stdin.readline())

for i in range(T):
    n, m = map(int,sys.stdin.readline().split())
    room=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]
    print(room)
    result = 0
    i = 0
    j = 0
    while True:
        if room[i][j] == 0:
            i += 1
        if room[i][j] == 1:
            j += 1
        if i and j == n and m:
            i, j = -1, -1

        if room[i][j] == 0:
            i -= 1
        if room[i][j] == 1:
            j -= 1
        if i and j == 0 and 0:
            result += 1

    print(result)

