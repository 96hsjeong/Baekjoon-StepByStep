import sys

n, k = map(int, sys.stdin.readline().split())

if n // 2 < k:
    k = n - k

def solution(n, k):
    if k == 0 or n == k:
        return 1
    return solution(n-1, k) + solution(n-1, k-1)


answer = solution(n, k)

print(answer % 1000000007)