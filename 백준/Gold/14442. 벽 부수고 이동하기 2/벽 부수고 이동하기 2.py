from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, K))
    visit[0][0][K] = 1
    
    while queue:
        r, c, k = queue.popleft()

        if r == N-1 and c == M-1:
            return visit[r][c][k]
        
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not arr[nr][nc]: # 0
                if not visit[nr][nc][k]: # not visit: 
                    visit[nr][nc][k] = visit[r][c][k] + 1
                    queue.append((nr, nc, k))
            else: # 1
                if k and not visit[nr][nc][k-1]: # k and not visit
                    visit[nr][nc][k-1] = visit[r][c][k] + 1
                    queue.append((nr, nc, k-1))

    return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
delta = ((-1,0),(1,0),(0,-1),(0,1))
print(bfs())