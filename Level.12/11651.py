import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(tuple(map(int, sys.stdin.readline().split())))

data.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(*data[i])
