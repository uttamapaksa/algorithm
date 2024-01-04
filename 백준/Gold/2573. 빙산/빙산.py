def adjSea(r, c):
    adj = 0
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and not ice[nr][nc]:
            adj += 1
    return adj


def meltIce():
    melted = []
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                melted.append((i, j, adjSea(i, j)))

    for r, c, w in melted:
        if ice[r][c] > w:
            ice[r][c] -= w
        else:
            ice[r][c] = 0
            global cnt
            cnt -= 1


def is_one():
    stack = []
    visit = set()
    for i in range(N):
        if stack:
            break
        for j in range(M):
            if ice[i][j]:
                stack.append((i, j))
                visit.add((i, j))
                break

    while stack:
        r, c = stack.pop()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and ice[nr][nc] and (nr, nc) not in visit:
                stack.append((nr, nc))
                visit.add((nr, nc))

    if len(visit) == cnt:
        return 1
    return 0


def bfs():
    day = 0
    while cnt:
        if not is_one():
            return day
        meltIce()
        day += 1

    return 0


N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
cnt = sum(1 for r in ice for c in r if c)
d = ((-1, 0), (0, -1), (1, 0), (0, 1))
print(bfs())