N = int(input())
arr = [*map(int, input().split())]

G = [set() for _ in range(N)]
P = list(range(N))
exist = [1] * N

for i in range(N):
    if arr[i] == -1:
        continue
    G[arr[i]].add(i)
    P[i] = arr[i]

M = int(input())
stack = [M]
while stack:
    u = stack.pop()
    G[P[u]].discard(u)
    exist[u] = 0
    for v in G[u]:
        stack.append(v)

answer = 0
for i in range(N):
    if exist[i] and len(G[i]) == 0:
        answer += 1

print(answer)