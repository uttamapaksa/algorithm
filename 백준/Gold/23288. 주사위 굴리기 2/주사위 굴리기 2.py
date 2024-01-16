def rotate_dice():
    global d
    if bot > arr[x][y]:
        d = (d+1) % 4
    elif bot < arr[x][y]:
        d = (d+3) % 4


def move_dice():
    global top, bot, left, right, up, down, x, y, d, ans
    # x, y, d
    dx, dy = delta[d]
    x, y = x + dx, y + dy
    if x < 0 or x >= N or y < 0 or y >= M:
        x, y = x - dx*2, y - dy*2
        d = (d+2) % 4

    # top, bot, left, right, up, down
    if not d:
        top, bot, left, right, up, down = left, right, bot, top, up, down
    elif d == 1:
        top, bot, left, right, up, down = up, down, left, right, bot, top
    elif d == 2:
        top, bot, left, right, up, down = right, left, top, bot, up, down
    else:
        top, bot, left, right, up, down = down, up, left, right, top, bot

    # score
    ans += score_table[x][y] 


def make_score_table():
    for x in range(N):
        for y in range(M):
            if not score_table[x][y]:
                num = arr[x][y]
                stack = [(x, y)]
                visit = {(x, y)}

                while stack:
                    r, c = stack.pop()
                    for dr, dc in delta:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == num and (nr, nc) not in visit:
                            stack.append((nr, nc))
                            visit.add((nr, nc))
                
                score = num * len(visit)
                for r, c in visit:
                    score_table[r][c] = score


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
score_table = [[0] * M for _ in range(N)]
x = y = d = ans = 0
top, bot, left, right, up, down = 1, 6, 4, 3, 2, 5
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

make_score_table()
for _ in range(K):
    move_dice()
    rotate_dice()

print(ans)