# 에라토스테네스의 체
import sys

m, n = map(int, sys.stdin.readline().split())

sieve = [True] * (n + 1)
sieve[0] = False
sieve[1] = False

prime = []

for i in range(2, n + 1):
    if sieve[i]:
        prime.append(i)
        for j in range(i * 2, n + 1, i):
            sieve[j] = False

for p in prime:
    if m <= p <= n:
        print(p)
