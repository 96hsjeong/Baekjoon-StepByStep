import sys

n = sys.stdin.readline()
n_list = sys.stdin.readline().split()
m = sys.stdin.readline()
m_list = sys.stdin.readline().split()

n_list.sort()


def binary_search(search, start, end):
    if start > end:
        return 0

    mid = int((start + end) / 2)

    if n_list[mid] == search:
        return 1
    elif n_list[mid] > search:
        return binary_search(search, start, mid-1)
    else:
        return binary_search(search, mid+1, end)


for item in m_list:
    print(binary_search(item, 0, len(n_list)-1))
