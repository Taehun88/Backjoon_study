from collections import deque

cardnum = int(input())
deck = deque([i for i in range(1, cardnum+1)])

while len(deck) > 1:
    deck.popleft()
    move = deck.popleft()
    deck.append(move)

print(deck[0])