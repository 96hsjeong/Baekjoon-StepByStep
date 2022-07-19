import sys


def get_gcd(a, b):
    if a < b:
        a, b = b, a

    a, b = b, a % b

    if b == 0:
        return a
    else:
        return get_gcd(a, b)


n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

gap = [data[i] - data[i-1] for i in range(1, n)]
gcd = gap[0]

for i in range(1, n-1):
    gcd = get_gcd(gap[i], gcd)

answer = [gcd]

for n in range(2, int(gcd ** 0.5) + 1):
    if gcd % n == 0:
        answer.append(n)
        if n != gcd // n:
            answer.append(gcd // n)

answer.sort()

print(*answer)
