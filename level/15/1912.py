import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [-999] * n
dp[0] = A[0]

for i in range(1, n):
    if dp[i - 1] >= 0:
        dp[i] = dp[i - 1] + A[i]
    else:
        dp[i] = A[i]

print(max(dp))
