from heapq import heappop, heappush

N, M, X = map(int, input().split())
G = {i: [] for i in range(1, N+1)}
T = [0]  # 소요시간 리스트

# 그래프 간선 저장
for _ in range(M):
    s, e, t = map(int, input().split())
    G[s].append((t, e))

# 모든 마을 -> X 마을 소요시간 다익스트라
for s in range(1, N+1):
    D = [1000001] * (N+1)
    D[s] = 0
    V = set()
    Q = [(0, s)]
    while Q:
        t, s = heappop(Q)
        if s == X: break
        if s in V: continue
        V.add(s)
        for w, e in G[s]:
            if D[e] > t + w:
                D[e] = t + w
                heappush(Q, (D[e], e))
    T.append(D[X])

# X 마을 -> 모든 마을 소요시간 다익스트라
D = [1000001] * (N+1)
D[X] = 0
V = set()
Q = [(0, X)]
while Q:
    t, s = heappop(Q)
    if s in V: continue
    V.add(s)
    for w, e in G[s]:
        if D[e] > t + w:
            D[e] = t + w
            heappush(Q, (D[e], e))

# X -> 전체, 전체 -> X 소요시간을 더해서 최댓값 갱신
ans = 0
for i in range(1, N+1):
    T[i] += D[i]
    if T[i] > ans:
        ans = T[i]

print(ans)