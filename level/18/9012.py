import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = list(sys.stdin.readline().rstrip())
    stack = []
    vps = True

    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                vps = False
                break

    if stack:
        vps = False

    if vps:
        print("YES")
    else:
        print("NO")
