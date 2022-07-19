import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n + 1)]
p_list = list(permutations(data, m))

for p in p_list:
    print(*p)
