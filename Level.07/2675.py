import sys

T = int(input())
for i in range(T):
    R, S = sys.stdin.readline().split()
    for s in S:
        print(s * int(R), end="")
    print()