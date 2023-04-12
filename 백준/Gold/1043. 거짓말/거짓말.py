from collections import deque

N, M = map(int, input().split())
T = [*map(int, input().split())]
del T[0]
T = set(T)
party = []
ans = 0

for _ in range(M):
    tmp = [*map(int, input().split())]
    del tmp[0]
    tmp = set(tmp)
    party.append(tmp)

visit = [0] * len(party)
q = deque([T])
while q:
    now = q.popleft()
    for i in range(len(party)):
        if visit[i]: continue
        new = party[i]
        if now & new:
            T = T.union(new)
            visit[i] = 1
            M -= 1
            q.append(new)

print(M)