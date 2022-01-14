word = input()
time = 0
ls = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for alphabet in word:
    for i in range(len(ls)):
        if alphabet in ls[i]:
            time += i + 3

print(time)