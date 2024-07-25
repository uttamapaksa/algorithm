from collections import deque

def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

def sol():
    global id, queue
    stack = [ls[0]]
    while stack:
        r, c = stack.pop()
        for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if arr[nr][nc] == 2: return 0
            if not arr[nr][nc] or visit[nr][nc]: continue
            visit[nr][nc] = 1
            arr[nr][nc] = 1
            stack.append((nr, nc))
            queue.append((nr, nc))
    stack = [ls[1]]
    while stack:
        r, c = stack.pop()
        for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if arr[nr][nc] == 1: return 0
            if not arr[nr][nc] or visit[nr][nc]: continue
            visit[nr][nc] = 1
            arr[nr][nc] = 2
            stack.append((nr, nc))
            queue.append((nr, nc))

    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                id += 1
                par.append(id)
                visit[i][j] = 1
                arr[i][j] = id
                stack = [(i, j)]
                queue.append((i, j))
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                        if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                        if not arr[nr][nc] or visit[nr][nc]: continue
                        visit[nr][nc] = 1
                        arr[nr][nc] = id
                        stack.append((nr, nc))
                        queue.append((nr, nc))
    
    while queue:
        nextq = deque()
        for r, c in queue:
            a = find(arr[r][c])
            for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
                if visit[nr][nc]:
                    b = find(arr[nr][nc])
                    if a == b: continue
                    if a != b:
                        # 끝
                        if (a == 1 and b == 2) or (a == 2 and b == 1):
                            return max(visit[r][c], visit[nr][nc]) - 1
                        if a < b:
                            par[b] = a
                        else:
                            par[a] = b
                    continue
                visit[nr][nc] = visit[r][c] + 1
                arr[nr][nc] = a
                nextq.append((nr, nc))
        queue = nextq


R, C = map(int, input().split())
par = [0]
visit = [[0] * C for _ in range(R)]
arr = [[*input()] for _ in range(R)]
ls = []
id = 0
queue = deque()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'X':
            arr[i][j] = 0
        elif arr[i][j] == 'L':
            id += 1
            par.append(id)
            visit[i][j] = 1
            arr[i][j] = id
            ls.append((i, j))
            queue.append((i, j))
print(sol())