import sys

n = int(sys.stdin.readline())
answer = 0

while n >= 5:
    n //= 5
    answer += n

print(answer)