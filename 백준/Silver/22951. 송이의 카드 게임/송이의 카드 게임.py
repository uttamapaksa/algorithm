N, K = map(int, input().split()); L = N*K
next = [i+1 for i in range(L)]; next[-1] = 0
cards = []
id = 0
for _ in range(N):
    for val in map(int, input().split()):
        cards.append([id, val])
        id += 1

id = L-1
for _ in range(L):
    val = cards[next[id]][1]
    next[id] = next[next[id]]
    for _ in range(val-1):
        id = next[id]

a, b = cards[next[id]]
print(a//K+1, b)