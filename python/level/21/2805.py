import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

max_h = 0

while start <= end:
    mid = (start + end) // 2

    sliced = sum([t - mid if t > mid else 0 for t in tree])

    if m <= sliced and max_h < mid:
        max_h = mid

    if m == sliced:
        break
    elif m < sliced:
        start = mid + 1
    else:
        end = mid - 1

print(max_h)
