def bubble_sort(data):
    swap = False
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True

        if not swap:
            break

    return data

def insert_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break

    return data

def select_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

    return data


n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

# data = bubble_sort(data)
# data = insert_sort(data)
data = select_sort(data)

for i in range(len(data)):
    print(data[i])
