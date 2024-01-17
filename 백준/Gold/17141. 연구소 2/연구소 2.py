from itertools import combinations
from collections import deque


def bfs():
    global ans

    for comb in combinations(virus, M):
        queue = deque()
        visit = set()

        for x, y in comb:
            queue.append((x, y, 0))
            visit.add(x*N+y)

        while queue:
            r, c, t = queue.popleft()
            if t >= ans: break
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and nr*N+nc not in visit:
                    queue.append((nr, nc, t+1))
                    visit.add(nr*N+nc)
        else:
            if len(visit) == total:
                ans = min(ans, t)

        
def is_possible():
    group = 0
    visit = set()

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1 or x*N+y in visit: continue
            stack = [(x, y)]
            visit.add(x*N+y)
            group += 1
            virus_found = 0

            while stack:
                r, c = stack.pop()
                if arr[r][c] == 2:
                    virus_found = 1
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and nr*N+nc not in visit:
                        stack.append((nr, nc))
                        visit.add(nr*N+nc)
            if not virus_found:
                return 0

    if M < group:
        return 0
    else:
        return 1    


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
zero = sum(1 for row in arr for ele in row if not ele)
total = len(virus) + zero
ans = N**2
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

if is_possible():
    bfs()
    print(ans)
else:
    print(-1)