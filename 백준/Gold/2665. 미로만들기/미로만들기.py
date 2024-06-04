def dfs():
    curr = [(0, 0)]
    visit = [[-1] * N for _ in range(N)]
    visit[0][0] = 0

    while True:
        next = []
        while curr:
            r, c = curr.pop()
            if r == N-1 and c == N-1:
                return visit[r][c]
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                if visit[nr][nc] != -1: continue
                if arr[nr][nc]:  # room
                    curr.append((nr, nc))
                    visit[nr][nc] = visit[r][c]
                else:  # wall
                    next.append((nr, nc))
                    visit[nr][nc] = visit[r][c] + 1
        curr = next


N = int(input())
arr = [[*map(int, [*input()])] for _ in range(N)]
print(dfs())