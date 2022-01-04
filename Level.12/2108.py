import sys
from collections import Counter
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    item = int(sys.stdin.readline())
    data.append(item)

data.sort()
count = Counter(data).most_common(2)

print(round(sum(data)/n))
print(data[int(len(data)/2)])

if len(count) >= 2:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(data[-1] - data[0])
