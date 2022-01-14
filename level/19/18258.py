import sys
from collections import deque

queue = deque()

n = int(sys.stdin.readline())

for _ in range(n):
    inputs = sys.stdin.readline().split()
    cmd = inputs[0]
    if cmd == 'push':
        x = int(inputs[1])
        queue.append(x)
    elif cmd == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
