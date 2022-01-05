import sys
n = int(sys.stdin.readline())
data = set()
for _ in range(n):
    data.add(sys.stdin.readline().rstrip())

data = list(data)
data.sort(key=lambda x: (len(x), x))

for item in data:
    print(item)