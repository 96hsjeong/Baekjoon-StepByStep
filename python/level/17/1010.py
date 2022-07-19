import sys

T = int(sys.stdin.readline())
dp = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[m][n])
