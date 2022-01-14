import sys

s = list(sys.stdin.readline().rstrip())

for i in range(1, 27):
    if chr(i+96) in s:
        print(s.index(chr(i+96)), end=" ")
    else:
        print(-1, end=" ")
