from collections import deque


def bfs():
    queue = deque()
    queue.append((K, 0, 0, 1))
    visit[K][0][0] = 1
    
    while queue:
        k, r, c, cnt = queue.popleft()

        if r == N-1 and c == M-1:
            return cnt
        
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not arr[nr][nc]: # 0
                if not visit[k][nr][nc]: # not visit: 
                    visit[k][nr][nc] = cnt+1
                    queue.append((k, nr, nc, cnt+1))
            else: # 1
                if k and not visit[k-1][nr][nc]: # k and not visit
                    if (cnt & 1): # odd: day
                        visit[k-1][nr][nc] = cnt+1
                        queue.append((k-1, nr, nc, cnt+1))
                    else: # even: night
                        queue.append((k, r, c, cnt+1))

    return -1


N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[[0] * M for _ in range(N)] for _ in range(K+1)]
delta = ((-1,0),(1,0),(0,-1),(0,1))
print(bfs())