import sys
from math import sqrt

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance == 0 and r1 == r2:
        print(-1)
    elif distance > max(r1, r2):
        if distance == r1 + r2:
            print(1)
        elif distance > r1 + r2:
            print(0)
        else:
            print(2)
    else:
        if distance == max(r1, r2) - min(r1, r2):
            print(1)
        elif distance > max(r1, r2) - min(r1, r2):
            print(2)
        else:
            print(0)
