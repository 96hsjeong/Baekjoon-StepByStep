import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split())))

data.sort()

for i in range(n):
    print(*data[i])
