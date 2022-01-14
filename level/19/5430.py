import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p_list = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    x = sys.stdin.readline().rstrip()
    if n == 0:
        arr = []
    else:
        arr = deque(x[1:-1].split(','))
    error = False
    reverse = False

    for p in p_list:
        if p == 'R':
            reverse = not reverse
        else:
            if not arr:
                error = True
                break

            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if error:
        print("error")
    else:
        if reverse:
            arr.reverse()
        print(f"[{','.join(arr)}]")
