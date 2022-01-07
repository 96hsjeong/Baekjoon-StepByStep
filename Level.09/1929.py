# 에라토스테네스의 체
import sys

m, n = map(int, sys.stdin.readline().split())

eratos = [True] * (n + 1)
eratos[0] = False
eratos[1] = False

prime = []

for i in range(2, n + 1):
    if eratos[i]:
        prime.append(i)
        for j in range(i * 2, n + 1, i):
            eratos[j] = False

for p in prime:
    if m <= p <= n:
        print(p)
