import sys
from collections import Counter

n = sys.stdin.readline()
n_list = sys.stdin.readline().split()
m = sys.stdin.readline()
m_list = sys.stdin.readline().split()

counter = Counter(n_list)
result = []

for item in m_list:
    result.append(counter[item])

print(*result)
