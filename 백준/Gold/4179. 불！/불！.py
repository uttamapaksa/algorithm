from collections import deque

R, C = map(int, input().split())
arr = [[*input()] for _ in range(R)]
q = deque()
for i in range(R):
    for j in range(C):
        tmp = arr[i][j]
        if tmp == '#':
            arr[i][j] = 1
        elif tmp == '.':
            arr[i][j] = 0
        elif tmp == 'J':
            arr[i][j] = 0
            q.appendleft((1, i, j, 1))
        else:
            arr[i][j] = 1
            q.append((0, i, j, 1))

escape = 0
while q:
    J, r, c, cnt = q.popleft()
    if J:
        if arr[r][c]: continue
        arr[r][c] = 1
        if r == 0 or r == R-1 or c == 0 or c == C-1:
            escape = 1
            print(cnt)
            break
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if nr < 0 or nr >= R or nc < 0 or nc >= C or arr[nr][nc]: continue
            q.append((1, nr, nc, cnt+1))
    else:
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if nr < 0 or nr >= R or nc < 0 or nc >= C or arr[nr][nc]: continue
            arr[nr][nc] = 1
            q.append((0, nr, nc, cnt))
if not escape: print('IMPOSSIBLE') 