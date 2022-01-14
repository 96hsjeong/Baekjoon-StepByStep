import sys

n, m = map(int, sys.stdin.readline().split())
A = []
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
B = []
for _ in range(m):
    B.append(list(map(int, sys.stdin.readline().split())))

answer = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            answer[x][y] += A[x][z] * B[z][y]

for i in range(n):
    print(*answer[i])
