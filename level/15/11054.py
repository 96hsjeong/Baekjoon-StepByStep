import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp_ascend = [0] * N
dp_descend = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dp_ascend[i] < dp_ascend[j]:
            dp_ascend[i] = dp_ascend[j]
    dp_ascend[i] += 1

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j] and dp_descend[i] < dp_descend[j]:
            dp_descend[i] = dp_descend[j]
    dp_descend[i] += 1

result = [dp_ascend[i] + dp_descend[i] - 1 for i in range(N)]

print(max(result))