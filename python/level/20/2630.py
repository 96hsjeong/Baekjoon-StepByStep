import sys

n = int(sys.stdin.readline())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

white = 0
blue = 0


def solution(x, y, n):
    global white, blue

    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                half = n // 2
                solution(x, y, half)
                solution(x, y+half, half)
                solution(x+half, y, half)
                solution(x+half, y+half, half)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


solution(0, 0, n)

print(white)
print(blue)
