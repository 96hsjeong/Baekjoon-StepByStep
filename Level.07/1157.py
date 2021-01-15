x = input().upper()

max_cnt = 0
for i in range(65, 91):
    cnt = x.count(chr(i))
    if max_cnt < cnt:
        max_cnt = cnt
        answer = chr(i)
    elif max_cnt == cnt:
        answer = '?'

print(answer)