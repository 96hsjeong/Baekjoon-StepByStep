import sys

x, y, w, h = map(int, sys.stdin.readline().split())

top = h - y
bottom = y
left = x
right = w - x

result = min(top, bottom, left, right)

print(result)