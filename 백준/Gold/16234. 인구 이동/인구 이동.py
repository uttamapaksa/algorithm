import sys; input = sys.stdin.readline
from collections import deque
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

N, L, R = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]

day = 0
moved = True
Q = deque()

while moved:
    moved = False
    V = set()

    for x in range(N):
        for y in range(N):
            if (x, y) in V: continue
            
            Q.append((x, y))
            V.add((x, y))
            M = {(x, y)}

            while Q:
                r, c = Q.popleft()
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in V: continue
                    if L <= abs(arr[r][c] - arr[nr][nc]) <= R:
                        Q.append((nr, nc))
                        V.add((nr, nc))
                        M.add((nr, nc))
            
            if len(M) > 1:
                moved = True
                avg = sum(arr[r][c] for r, c in M) // len(M)
                for r, c in M:
                    arr[r][c] = avg

    if moved: day += 1

print(day)