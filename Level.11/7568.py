import sys

n = int(sys.stdin.readline())

data = []
rank = [1] * n
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            rank[i] += 1
        elif data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            rank[j] += 1
        else:
            continue

print(*rank)