from collections import deque

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))
row = deque([0, 0, 0, 0]) # left, top, right, bottom
col = deque([0, 0, 0, 0]) # up, top, down, bottom
delta = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

for order in orders:
    dx, dy = delta[order]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
    x, y = nx, ny
    
    if order == 1: # east
        row.appendleft(row.pop())
        if not arr[x][y]:
            arr[x][y] = row[3]
        else:
            row[3] = arr[x][y]
            arr[x][y] = 0
        col[1], col[3] = row[1], row[3] # synchronize top and bottom

    elif order == 2:
        row.append(row.popleft())
        if not arr[x][y]:
            arr[x][y] = row[3]
        else:
            row[3] = arr[x][y]
            arr[x][y] = 0
        col[1], col[3] = row[1], row[3]

    elif order == 3:
        col.append(col.popleft())
        if not arr[x][y]:
            arr[x][y] = col[3]
        else:
            col[3] = arr[x][y]
            arr[x][y] = 0
        row[1], row[3] = col[1], col[3]

    else:
        col.appendleft(col.pop())
        if not arr[x][y]:
            arr[x][y] = col[3]
        else:
            col[3] = arr[x][y]
            arr[x][y] = 0
        row[1], row[3] = col[1], col[3]
    
    print(row[1])