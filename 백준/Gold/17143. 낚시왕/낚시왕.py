R, C, M = map(int, input().split())
delta = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}
turn = {1: 2, 2: 1, 3: 4, 4: 3}
shark = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d < 3:
        s %= ((R-1) * 2)
    else:
        s %= ((C-1) * 2)
    shark[r-1][c-1].append((s, d, z, 0))
ans = 0


def catch_shark(j):
    global ans
    for i in range(R):
        if shark[i][j]:
            ans += shark[i][j][0][2]
            shark[i][j] = []
            return


def move_shark(j):
    for r in range(R):
        for c in range(C):
            for s, d, z, jidx in shark[r][c]:
            # 순회 중에 리스트 크기가 변하지만 주소는 그대로라서 오류 아님
                if jidx == j:
                    nr, nc, nd = r, c, d
                    for _ in range(s):
                        nr, nc = nr + delta[nd][0], nc + delta[nd][1]
                        if nr < 0 or nr >= R or nc < 0 or nc >= C:
                            nd = turn[nd]
                            nr, nc = nr + delta[nd][0] * 2, nc + delta[nd][1] * 2
                    shark[r][c].remove((s, d, z, jidx))
                    shark[nr][nc].append((s, nd, z, jidx+1))


def eat_shark():
    for r in range(R):
        for c in range(C):
            if shark[r][c]:
                shark[r][c].sort(key=lambda x: x[2], reverse=True)
                shark[r][c] = [shark[r][c][0]]


for j in range(C):
    catch_shark(j)
    move_shark(j)
    eat_shark()

print(ans)