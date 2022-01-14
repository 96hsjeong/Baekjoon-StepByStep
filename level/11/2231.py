import sys

n = int(sys.stdin.readline())

result = 0

for i in range(1, len(str(n)) * 9 + 1):
    x = n - i
    if x < 0:
        break
    p_sum = x + sum(map(int, str(x)))
    if p_sum == n:
        result = x

print(result)