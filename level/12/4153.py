import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break

    length = [a, b, c]
    max_i = length.index(max(length))
    calculate = 0
    for i in range(3):
        if i == max_i:
            calculate -= length[i] ** 2
        else:
            calculate += length[i] ** 2

    if calculate == 0:
        print("right")
    else:
        print("wrong")






