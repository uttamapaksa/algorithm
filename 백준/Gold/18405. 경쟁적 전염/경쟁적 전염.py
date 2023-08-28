from collections import deque

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X, Y = X-1, Y-1
A = 0

if arr[X][Y]:
    print(arr[X][Y])
else:
    arr[X][Y] = -1
    Q = deque([(0, X, Y)])
    while Q:
        t, r, c = Q.popleft()
        if t == S: break
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= K or arr[nr][nc] == -1: continue
            if arr[nr][nc] > 0:
                if not A: A = arr[nr][nc]
                else: A = min(A, arr[nr][nc])
                S = t + 1
                arr[nr][nc] = -1
            else:
                Q.append((t+1, nr, nc))
                arr[nr][nc] = -1
    print(A)