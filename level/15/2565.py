import sys

n = int(sys.stdin.readline())
wire = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    wire.append((a, b))

wire.sort(key=lambda x: x[0])

dp_ascend = [0] * n
dp_descend = [0] * n

for i in range(n):
    for j in range(i):
        if wire[i][0] > wire[j][0] and wire[i][1] > wire[j][1] and dp_ascend[i] < dp_ascend[j]:
            dp_ascend[i] = dp_ascend[j]
    dp_ascend[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if wire[i][0] > wire[j][0] and wire[i][1] > wire[j][1] and dp_descend[i] < dp_descend[j]:
            dp_descend[i] = dp_descend[j]
    dp_descend[i] += 1

print(n - max(max(dp_ascend), max(dp_descend)))