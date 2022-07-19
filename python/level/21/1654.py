import sys

k, n = map(int, sys.stdin.readline().split())
data = []
for _ in range(k):
    data.append(int(sys.stdin.readline()))

start = 1
end = max(data)
max_len = 0

while start <= end:
    mid = (start + end) // 2

    count = 0

    for i in range(k):
        count += data[i] // mid

    if n <= count and max_len < mid:
        max_len = mid

    if n <= count:
        start = mid + 1
    else:
        end = mid - 1

print(max_len)
