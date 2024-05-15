from collections import deque

def solution(arr) -> int:
    
    def path_len(si: int, sj: int, ei: int, ej: int) -> int:
        v = [[0] * m for _ in range(n)]
        v[si][sj] = 1
        q = deque([(si, sj)])
        while q:
            r, c = q.popleft()
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] == 'X' or v[nr][nc]:
                    continue
                if nr == ei and nc == ej:
                    return v[r][c]
                v[nr][nc] = v[r][c] + 1
                q.append((nr, nc))
        return 0
    
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'S':
                si, sj = i, j
            elif arr[i][j] == 'L':
                li, lj = i, j
            elif arr[i][j] == 'E':
                ei, ej = i, j
    
    stol = path_len(si, sj, li, lj)
    if stol:
        ltoe = path_len(li, lj, ei, ej)
        if ltoe:
            return stol + ltoe
    return -1