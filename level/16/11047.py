import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

count = 0

for i in range(len(coins)-1, -1, -1):
    if k/coins[i] >= 1:
        count += int(k/coins[i])
        k %= coins[i]

print(count)
            