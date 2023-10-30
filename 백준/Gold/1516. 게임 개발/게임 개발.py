from collections import deque

N = int(input())
T = {}
C = {i: [] for i in range(1, N+1)}
P = {i: 0 for i in range(1, N+1)}

# 가중치(T), 인접노드(C), 진입차수(P)
for i in range(1, N+1):
    tmp = [*map(int, input().split())]
    T[i] = tmp[0]
    for j in tmp[1:-1]:
        C[j].append(i)
        P[i] += 1

# 시작노드(Q)
Q = deque()
for i in P:
    if not P[i]:
        Q.append(i)

# 위상정렬 + 그리디
ans = {i: T[i] for i in range(1, N+1)}
while Q:
    s = Q.popleft()
    for e in C[s]:
        P[e] -= 1
        ans[e] = max(ans[e], ans[s] + T[e])
        if not P[e]:
            Q.append(e)

for i in range(1, N+1):
    print(ans[i])