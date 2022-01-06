def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False

    return True


n = int(input())
m = int(input())
prime_list = []

for num in range(n, m+1):
    if isPrime(num):
        prime_list.append(num)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))