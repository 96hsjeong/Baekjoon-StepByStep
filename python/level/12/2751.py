def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = [], []

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)

    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)


def merge(left, right):
    lp, rp = 0, 0
    data = []

    while len(left) > lp and len(right) > rp:
        if left[lp] < right[rp]:
            data.append(left[lp])
            lp += 1
        else:
            data.append(right[rp])
            rp += 1

    while len(left) > lp:
        data.append(left[lp])
        lp += 1

    while len(right) > rp:
        data.append(right[rp])
        rp += 1

    return data


n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

# data = quick_sort(data)
# data = merge_sort(data)
data.sort()

for i in range(len(data)):
    print(data[i])