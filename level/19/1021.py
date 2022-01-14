import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
pick = list(map(int, sys.stdin.readline().split()))
dq = deque([i for i in range(1, n+1)])

count = 0

while pick:
    i = dq.index(pick[0])
    if i == 0:
        x = dq.popleft()
        pick.remove(x)
    elif i <= int(len(dq)//2):
        for _ in range(i):
            x = dq.popleft()
            dq.append(x)
            count += 1
    else:
        for _ in range(len(dq) - i):
            x = dq.pop()
            dq.appendleft(x)
            count += 1

print(count)