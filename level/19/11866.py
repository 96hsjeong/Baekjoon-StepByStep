import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([str(i) for i in range(1, n + 1)])
result = []
while queue:
    for i in range(1, k + 1):
        x = queue.popleft()
        if i == k:
            result.append(x)
        else:
            queue.append(x)

print(f"<{', '.join(result)}>")