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
ring = list(map(int, sys.stdin.readline().split()))

first = ring[0]

for i in range(1, n):
    gcd = get_gcd(first, ring[i])
    print(f"{first//gcd}/{ring[i]//gcd}")