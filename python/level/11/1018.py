import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

result = 1e9

for r in range(n - 7):
    for c in range(m - 7):
        case1 = 0  # 1행 1열이 W인 경우
        case2 = 0  # 1행 1열이 B인 경우

        for i in range(r, r + 8):
            for j in range(c, c + 8):
                row_is_odd = i % 2 == 1
                row_is_even = i % 2 == 0
                col_is_odd = j % 2 == 1
                col_is_even = j % 2 == 0
                if (row_is_odd and col_is_odd) or (row_is_even and col_is_even):
                    if board[i][j] == 'B':
                        case1 += 1
                    else:
                        case2 += 1
                else:
                    if board[i][j] == 'W':
                        case1 += 1
                    else:
                        case2 += 1

        if min(case1, case2) < result:
            result = min(case1, case2)

print(result)