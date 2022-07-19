import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    clothes = dict()
    for _ in range(n):
        cloth, type = sys.stdin.readline().split()
        if type not in clothes:
            clothes[type] = ['naked']

        clothes[type].append(cloth)

    answer = 1
    for v in clothes.values():
        answer *= len(v)

    print(answer - 1)
