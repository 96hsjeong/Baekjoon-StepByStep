import sys

while True:
    inputs = list(sys.stdin.readline().rstrip())

    if inputs == ['.']:
        break

    stack = []
    ps = ['(', ')', '[', ']']
    vps = True

    for i in inputs:
        if i not in ps:
            continue

        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                vps = False
                break
        else:
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                vps = False
                break

    if stack:
        vps = False

    if vps:
        print('yes')
    else:
        print('no')
