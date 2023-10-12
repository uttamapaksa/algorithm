from collections import deque

def BFS():
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= L or nc < 0 or nc >= L or V[nr][nc]: continue
            Q.append((nr, nc))
            V[nr][nc] = V[r][c] + 1
            if nr == r2 and nc == c2:
                return V[nr][nc] - 100
    return 0
            
T = int(input())
for _ in range(T):
    L = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    V = [[0] * L for _ in range(L)]
    Q = deque([(r1, c1)])
    V[r1][c1] = 100

    print(BFS())
