import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))

min_oil_price = 1e9
total_cost = 0

for i in range(n-1):
    if oil_price[i] < min_oil_price:
        min_oil_price = oil_price[i]

    total_cost += min_oil_price * distance[i]

print(total_cost)