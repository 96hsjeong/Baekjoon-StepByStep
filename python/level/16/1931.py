import sys

n = int(sys.stdin.readline())
schedule = []
for _ in range(n):
    schedule.append(tuple(map(int, sys.stdin.readline().split())))

schedule.sort(key=lambda x: (x[1], x[0]))

count = 1
end = schedule[0][1]

for i in range(1, n):
    if end <= schedule[i][0]:
        count += 1
        end = schedule[i][1]

print(count)
