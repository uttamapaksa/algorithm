from collections import deque
# input
H, W = map(int, input().split())
arr = [[*input()] for _ in range(H)]
delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
# convert to numbers
water = deque()
for i in range(H):
    for j in range(W):
        if arr[i][j] == '.':
            arr[i][j] = 0
            # add water
            water.append((i, j, 0))
        else:
            arr[i][j] = int(arr[i][j])
# BFS
w = 0
while water:
    r, c, w = water.popleft()
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= H or nc < 0 or nc >= W or not arr[nr][nc]: continue
        arr[nr][nc] -= 1
        if not arr[nr][nc]:
            water.append((nr, nc, w+1))
# output
print(w)