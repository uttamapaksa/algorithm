from collections import deque

answer = ""
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
tc = int(input())
for _ in range(tc):
    cnt = 0

    # input
    h, w = map(int, input().split())
    arr = [[*input()] for _ in range(h)]
    keys = {*map(ord, [*input()])}

    # convert to integer
    for i in range(h):
        for j in range(w):
            if arr[i][j] == "*": arr[i][j] = 1
            elif arr[i][j] == ".": arr[i][j] = 0
            elif arr[i][j] == "$": arr[i][j] = 2
            else: arr[i][j] = ord(arr[i][j])

    # start points
    porte = []
    visit = [[0] * w for _ in range(h)]
    for c in range(w):
        for r in (0, h-1):
            if arr[r][c] == 1: continue
            porte.append((r, c))
            visit[r][c] = 1
    for r in range(1, h-1):
        for c in (0, w-1):
            if arr[r][c] == 1: continue
            porte.append((r, c))
            visit[r][c] = 1

    # until a new key cannot be found
    findNewKey = 1
    while findNewKey:
        findNewKey = 0
        newVisit = [[*row] for row in visit]
        queue = deque(porte)

        while queue:
            r, c = queue.popleft()
            val = arr[r][c]
            # .
            if not val: pass
            # $
            elif val == 2: cnt += 1
            # upper
            elif val <= 90:
                if (val + 32) not in keys: continue
            # lower
            elif val not in keys: keys.add(val); findNewKey = 1
            arr[r][c] = 0
            # bfs
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= h or nc < 0 or nc >= w or newVisit[nr][nc] or arr[nr][nc] == 1: continue
                newVisit[nr][nc] = 1
                queue.append((nr, nc))

    # output
    answer += f'{cnt}\n'

print(answer)