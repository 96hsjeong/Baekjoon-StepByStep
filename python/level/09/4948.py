max_value = 123456 * 2
sieve = [True] * (max_value + 1)
sieve[0] = False
sieve[1] = False

m = int(max_value ** 0.5)

for i in range(2, m + 1):
    if sieve[i]:
        for j in range(2 * i, max_value + 1, i):
            sieve[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            cnt += 1
    print(cnt)