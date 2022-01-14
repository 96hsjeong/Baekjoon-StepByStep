import sys

sieve = [True] * 10001
sieve[0] = False
sieve[1] = False

for i in range(2, int(10000 ** 0.5) + 1):
    if sieve[i]:
        for j in range(2 * i, 10001, i):
            sieve[j] = False

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    x = n // 2
    y = n // 2
    while not (sieve[x] and sieve[y]):
        x -= 1
        y += 1

    print(x, y)
