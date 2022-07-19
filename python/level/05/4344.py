c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))
    avg = sum(data[1:]) / data[0]
    count = 0
    for score in data[1:]:
        if score > avg:
            count += 1
    print("{:.3f}%".format(count/data[0] * 100))