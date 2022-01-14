import sys


def five_count(n):
    count = 0
    while n >= 5:
        n = n // 5
        count += n
    return count


def two_count(n):
    count = 0
    while n >= 2:
        n = n // 2
        count += n
    return count


n, m = map(int, sys.stdin.readline().split())

five_cnt = five_count(n) - five_count(n - m) - five_count(m)
two_cnt = two_count(n) - two_count(n - m) - two_count(m)
answer = min(five_cnt, two_cnt)

print(answer)