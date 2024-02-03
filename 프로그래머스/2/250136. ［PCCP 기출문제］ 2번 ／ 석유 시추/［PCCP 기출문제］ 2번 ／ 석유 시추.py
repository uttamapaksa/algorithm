d = ((-1, 0), (0, -1), (1, 0), (0, 1))

def solution(arr):
    n = len(arr)
    m = len(arr[0])
    oil = [0] * (m+1)
    
    visit = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not arr[i][j] or visit[i][j]: continue
            
            S = [(i, j)]
            tmp = [(i, j)]
            tmpm = {j}
            visit[i][j] = 1
            
            while S:
                r, c = S.pop()
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and not visit[nr][nc]:
                        S.append((nr, nc))
                        tmp.append((nr, nc))
                        tmpm.add(nc)
                        visit[nr][nc] = 1
            
            cnt = len(tmp)
            for r, c in tmp:
                visit[r][c] = cnt
            for c in tmpm:
                oil[c] += cnt
    
    return max(oil)