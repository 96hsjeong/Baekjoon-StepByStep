import sys

n = int(sys.stdin.readline())
stack = []
result = []
num = 1
impossible = False

for _ in range(n):
    x = int(sys.stdin.readline())

    while True:
        if stack and stack[-1] == x:
            stack.pop()
            result.append('-')
            break
        elif not stack or stack[-1] < x:
            stack.append(num)
            result.append('+')
            num += 1
        else:
            impossible = True
            break

    if impossible:
        break

if impossible:
    print('NO')
else:
    for i in result:
        print(i)