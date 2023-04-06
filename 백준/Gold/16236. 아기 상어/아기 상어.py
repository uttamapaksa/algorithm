dr = (-1, 0, 0, 1)
dc = (0, -1, 1, 0)


def eat():
    global r, c, time, shark, exp
    while q:
        q.sort(key=lambda x: (x[2], x[0], x[1]))
        r, c, time = q.pop(0)
        v = arr[r][c]
        if 0 < v < shark:
            arr[r][c] = 0
            fish.remove(v)
            exp -= 1
            if not exp:
                shark += 1
                exp = shark
            return 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visit[nr][nc] or arr[nr][nc] > shark: continue
            visit[nr][nc] = 1
            q.append((nr, nc, time + 1))
    return 0


N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
shark, exp, time, fish = 2, 2, 0, []
for i in range(N):
    for j in range(N):
        tmp = arr[i][j]
        if 0 < tmp < 7: fish.append(tmp)
        elif tmp == 9: arr[i][j] = 0; r, c = i, j

while fish and min(fish) < shark:
    visit = [[0] * N for _ in range(N)]
    visit[r][c] = 1
    q = [(r, c, time)]
    pretiem = time
    if not eat():
        time = pretiem
        break
print(time)