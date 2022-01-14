n = int(input())
data = list(map(int, input().split()))

count = 0

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False

    return True


for num in data:
    if isPrime(num):
        count += 1

print(count)