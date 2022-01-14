import sys

n = int(input())

for i in range(n):
    data = list(sys.stdin.readline().rstrip())
    point = 0
    score = 0
    for i in data:
        if i == 'O':
            point += 1
            score += point
        else:
            point = 0
    print(score)
