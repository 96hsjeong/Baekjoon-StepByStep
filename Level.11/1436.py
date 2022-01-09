import sys

n = int(sys.stdin.readline())

end_num = '666'
num = 0
cnt = 0

while cnt < n:
    num += 1
    if end_num in str(num):
        cnt += 1

print(num)

