import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = 1
for i in range(1, N):
    max_ = 0
    for j in range(i):
        if A[i] > A[j] and max_ < dp[j]:
            max_ = dp[j]

    if max_ != 0:
        dp[i] = max_ + 1
    else:
        dp[i] = 1

print(max(dp))