from collections import deque


def bfs():
    while Q:
        r, c, cnt = Q.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if cnt == -1:  # water
                if arr[nr][nc] in {".", "S"}:
                    arr[nr][nc] = "*"
                    Q.append((nr, nc, -1))
            else:  # hedgehog
                if arr[nr][nc] == "D":
                    return cnt+1
                if arr[nr][nc] == ".":
                    arr[nr][nc] = "S"
                    Q.append((nr, nc, cnt+1))

    return "KAKTUS"


delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
N, M = map(int, input().split())
arr = [[*input()] for _ in range(N)]

Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == "*":
            Q.appendleft((i, j, -1))  # water
        elif arr[i][j] == "S":
            Q.append((i, j, 0))  # hedgehog

print(bfs())