def d(n: int):
    ls = [n]
    ls.extend([int(i) for i in str(n)])
    answer = sum(ls)
    return answer

s = set()

for i in range(1, 10000):
    item = d(i)
    s.add(item)

ls = [i for i in range(1, 10000) if i not in s]

for i in ls:
    print(i)
