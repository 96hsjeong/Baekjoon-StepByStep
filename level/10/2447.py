n = int(input())

matrix = [['*'] * n for _ in range(n)]

def print_star(r, c, n):
    if n <= 1:
        return
    m = n // 3
    for i in range(m, 2 * m):
        for j in range(m, 2 * m):
            matrix[r + i][c + j] = ' '

    for i in range(3):
        for j in range(3):
            print_star(r + i * m, c + j * m, m)

print_star(0, 0, n)

for row in matrix:
    print(''.join(row))
