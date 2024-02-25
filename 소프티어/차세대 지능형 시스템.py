n,t = map(int,input().split()) #격자 배열의 크기, 시간

signal = []
signal = [[list(map(int,input().split())) for _ in range(n)] for _ in range(n)]

signalInfo = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(13)]
# signalInfo[신호 인덱스][들어가는 방향][나오는 방향]
signalInfo[1][0][1] = signalInfo[1][0][2] = signalInfo[1][0][3] = 1
signalInfo[2][1][2] = signalInfo[2][1][3] = signalInfo[2][1][0] = 1
signalInfo[3][2][3] = signalInfo[3][2][0] = signalInfo[3][2][1] = 1
signalInfo[4][3][0] = signalInfo[4][3][1] = signalInfo[4][3][2] = 1

for i in range(4):
    signalInfo[i+5][i][(i+2)% 4] = 1
    signalInfo[i+5][i][(i+3)% 4] = 1
    signalInfo[i+9][i][(i+1)% 4] = 1
    signalInfo[i+9][i][(i+2)% 4] = 1

junction = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
junction[0][0][1] = 1
junction2 = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
visit[0][0] = 1
def update(time,row,col,inDir,outDir,junction,junction2):
    signalNow = signal[row][col][time%4]   #4가지 신호를 무한히 반복하기 땨뮨애 time%4, 4가지 신호를 무한 반복하니 signal[row][col][time%4]
    if signalInfo[signalNow][inDir][outDir]:  #현재 신호에 in, out이 1이고 그떄 out이 0이면 
        if outDir == 0 and col != 0:
            junction2[row][col-1][2] = 1
            visit[row][col-1] =1
        elif outDir == 1 and row != n-1:
            junction2[row+1][col][3] = 1
            visit[row+1][col] =1
        elif outDir == 2 and col != n-1:
            junction2[row][col+1][0] = 1
            visit[row][col+1] =1
        elif outDir ==3 and row != 0:
            junction2[row-1][col][1] = 1
            visit[row-1][col] =1
    return

for time in range(t):
    for row in range(n):
        for col in range(n):
            for inDir in range(4):
                if junction[row][col][inDir]:
                    for outDir in range(4):
                        update(time,row,col,inDir,outDir,junction,junction2)
                    junction[row][col][inDir] = 0
    junction, junction2 = junction2, junction

count = 0
for row in range(n):
    for col in range(n):
        if visit[row][col] == 1:
            count += 1
print(count)

#https://softeer.ai/practice/6274