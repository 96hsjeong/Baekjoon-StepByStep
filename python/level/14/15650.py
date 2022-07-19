import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n + 1)]
c_list = list(combinations(data, m))

for c in c_list:
    print(*c)
