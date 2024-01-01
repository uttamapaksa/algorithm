N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
land = [[] for _ in range(8)]
land_num = 1

# update array per land
def island(r, c):
    S = [(r, c)]
    arr[r][c] = land_num
    land[land_num].append((r, c))
    while S:
        r, c = S.pop()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] != 1: continue
            S.append((nr, nc))
            arr[nr][nc] = land_num
            land[land_num].append((nr, nc))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            land_num += 1
            island(i, j)

# update distances per land
D = [[99] * (land_num+1) for _ in range(land_num+1)]
for u in range(2, land_num+1):
    for r, c in land[u]:
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            dist = 0
            while 0 <= nr < N and 0 <= nc < M:
                v = arr[nr][nc]
                if v == u: break # same land
                if D[v][u] != 99: break # already updated
                if v: # update minimum path
                    if dist < 2: break # length shortage
                    D[u][v] = min(D[u][v], dist)
                    break
                nr, nc = nr + dr, nc + dc
                dist += 1

# find
P = [i for i in range(land_num+1)]
def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

# Kruskal Algorithm
G = [(D[i][j], i, j) for i in range(2, land_num+1) for j in range(i+1, land_num+1) if D[i][j] != 99]
G.sort()

cnt = ans = 0
for w, u, v in G:
    a, b = find(u), find(v)
    if a == b: continue
    P[a] = b
    cnt += 1
    ans += w

if cnt == land_num - 2: print(ans)
else: print(-1)