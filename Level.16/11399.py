import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()

result = 0

for i in range(n):
    result += p[i] * (n-i)

print(result)