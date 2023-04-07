import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
P = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([(1, tree[1])])
P[1] = 1
while q:
    v, child = q. popleft()
    for w in child:
        if P[w]: continue
        P[w] = v
        q.append((w, tree[w]))

for i in range(2, N+1):
    print(P[i])