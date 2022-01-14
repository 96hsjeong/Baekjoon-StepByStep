import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
deck = list(map(int, sys.stdin.readline().split()))

c_list = list(combinations(deck, 3))
gap = 1e9

for c in c_list:
    if 0 <= m-sum(c) < gap:
        gap = m - sum(c)

print(m - gap)
