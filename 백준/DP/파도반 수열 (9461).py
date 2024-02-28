K=int(input())
for _ in range(K):

    N= int(input())
    dp =[0] * 1000
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 2
    dp[5] = 3
    dp[6] = 4

    for index in range(6,1000):
        dp[index] = dp[index -2] + dp[index-3]

    print(dp[N-1])
