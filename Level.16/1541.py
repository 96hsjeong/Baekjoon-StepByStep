import sys

data = sys.stdin.readline().split('-')

result = 0

result += sum(map(int, data[0].split('+')))

for d in data[1:]:
    result -= sum(map(int, d.split('+')))

print(result)