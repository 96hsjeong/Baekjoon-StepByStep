import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    documents = deque([i for i in range(n)])
    importance = deque(map(int, sys.stdin.readline().split()))
    count = 0
    
    while True:
        d = documents.popleft()
        i = importance.popleft()

        if not importance:
            count += 1
            break

        if i < max(importance):
            documents.append(d)
            importance.append(i)
        else:
            count += 1
            if m == d:
                break

    print(count)
