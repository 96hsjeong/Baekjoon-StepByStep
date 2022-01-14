import sys

n, k = map(int, sys.stdin.readline().split())
answer = 1

if n - k < k:
    k = n - k

for i in range(k):
    answer *= n - i
    answer //= i + 1

print(answer)
