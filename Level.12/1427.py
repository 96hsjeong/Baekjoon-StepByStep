data = list(map(int, str(input())))
data.sort(reverse=True)
print(*data, sep='')