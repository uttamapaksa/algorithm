def explode() -> bool:
    global arr
    visit = [[0] * M for _ in range(N)]
    queues = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '.' or visit[r][c]: continue
            queue = [(r, c)]
            visit[r][c] = 1
            front = 0
            while front < len(queue):
                r, c = queue[front]
                front += 1
                for dr, dc in D:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
                    if visit[nr][nc] or arr[nr][nc] != arr[r][c]: continue
                    queue.append((nr, nc))
                    visit[nr][nc] = 1
            if len(queue) >= 4:
                queues.append(queue)

    if queues:
        for queue in queues:
            for r, c in queue:
                arr[r][c] = "."
        return True
    return False


def gravity() -> None:
    for c in range(M):
        for r in range(N-2, -1, -1):
            if arr[r][c] == '.': continue
            nr = r
            for tmpr in range(r+1, N):
                if arr[tmpr][c] == '.':
                    nr = tmpr
                else:
                    break
            if r != nr:
                arr[nr][c], arr[r][c] = arr[r][c], '.'


N, M, D = 12, 6, ((-1, 0), (0, -1), (1, 0), (0, 1))
arr = [[*input()] for _ in range(N)]
ans = 0

while explode():
    ans += 1
    gravity()

print(ans)