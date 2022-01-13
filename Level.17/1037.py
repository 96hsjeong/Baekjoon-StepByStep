import sys

n = int(sys.stdin.readline())
factor = list(map(int, sys.stdin.readline().split()))
factor.sort()

answer = factor[0] * factor[-1]

print(answer)