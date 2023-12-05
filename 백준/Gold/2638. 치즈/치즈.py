# input
N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
time = 0


def set_exposed_air():
    while exposed_air:
        r, c = exposed_air.pop()
        arr[r][c] = -1
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc]: continue
            arr[nr][nc] = -1
            exposed_air.append((nr, nc))
exposed_air = [(0, 0)]
set_exposed_air()


def set_cheese_list():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cheese.append((i, j))
cheese = []
set_cheese_list()


def melt_cheese():
    remain = []
    global cheese
    while cheese:
        r, c = cheese.pop() 
        air = 0
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] != -1: continue
            air += 1
            if air == 2: break
        if air < 2:
            remain.append((r, c))
        else:
            exposed_air.append((r, c))

    set_exposed_air()
    cheese = remain # update cheese_list


while cheese:
    time += 1
    melt_cheese()
    
print(time)