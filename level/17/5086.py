import sys

while True:
    x, y = map(int, sys.stdin.readline().split())

    if x == y:
        break

    if y % x == 0:
        print('factor')
    elif x % y == 0:
        print('multiple')
    else:
        print('neither')
