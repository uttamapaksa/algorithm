from collections import deque

def solution(arr):
    n, m = len(arr), len(arr[0])
    visit = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                si, sj = i, j
                break
    
    visit[si][sj] = 1
    q = deque([(si, sj, 1)])
    while q:
        r, c, k = q.popleft()
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr, nc = r, c
            while True:
                nr, nc = nr + dr, nc + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] == 'D':
                    nr, nc = nr - dr, nc - dc
                    if not visit[nr][nc]:
                        if arr[nr][nc] == 'G':
                            return k
                        visit[nr][nc] = 1
                        q.append((nr, nc, k+1))
                    break
    return -1