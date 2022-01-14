import sys
from collections import deque

n = int(sys.stdin.readline())

deck = deque([i for i in range(1, n+1)])

while len(deck) > 1:
    deck.popleft()
    card = deck.popleft()
    deck.append(card)

print(deck.popleft())