def Group_Word(w):
    for i in range(len(w)-1):
        index = w.find(w[i], i+1)
        if index != -1 and index != i+1:
            return False
    return True

n = int(input())
answer = 0
for i in range(n):
    w = input()
    if Group_Word(w):
        answer += 1
print(answer)