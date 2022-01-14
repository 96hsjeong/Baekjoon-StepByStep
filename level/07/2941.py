word = input()
ls = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
answer = 0
for a in ls:
    if a == 'z=':
        answer += word.count('z=') - word.count(('dz='))
    elif a in word:
        answer += word.count(a)
answer += len(word) - answer * 2 - word.count(('dz='))
print(answer)