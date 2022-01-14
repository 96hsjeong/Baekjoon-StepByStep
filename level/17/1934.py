import sys

def gcd(a, b):
    if a < b:
        a, b = b, a

    a, b = b, a % b

    if b == 0:
        return a
    else:
        return gcd(a, b)

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
    