import sys

n = int(sys.stdin.readline())
nge = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(n)]
stack = []

for i in range(n-1, -1, -1):
    while True:
        if not stack:
            stack.append(nge[i])
            break
        else:
            if stack[-1] <= nge[i]:
                stack.pop()
            else:
                result[i] = stack[-1]
                stack.append(nge[i])
                break

print(*result)
