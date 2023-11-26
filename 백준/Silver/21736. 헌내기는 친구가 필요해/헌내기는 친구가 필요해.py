from collections import deque

def sol():
    n, m = map(int, input().split())
    A = [input() for _ in range(n)]
    V = [[0] * m for _ in range(n)]

    def doyeon_idx():
        for i in range(n):
            for j in range(m):
                if A[i][j] == 'I':
                    return (i, j)
                
    i, j = doyeon_idx()
    Q = deque([(i, j)])
    V[i][j] = 1

    def bfs():
        ans = 0
        while Q:
            r, c = Q.popleft()
            for (dr, dc) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m or V[nr][nc] or A[nr][nc] == 'X': continue
                if A[nr][nc] == 'P':
                    ans += 1
                Q.append((nr, nc))
                V[nr][nc] = 1
        return ans or 'TT'
    
    print(bfs())

sol()