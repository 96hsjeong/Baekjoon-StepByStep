n = int(input())
scores = [0] * 300
for i in range(n):
    scores[i] = int(input())

dp = [0] * 300

dp[0] = scores[0]
dp[1] = scores[1] + dp[0]
dp[2] = max(scores[2] + dp[0], scores[2] + scores[1])

for i in range(3, n):
    dp[i] = max(scores[i] + dp[i - 2], scores[i] + scores[i - 1] + dp[i - 3])

print(dp[n - 1])
