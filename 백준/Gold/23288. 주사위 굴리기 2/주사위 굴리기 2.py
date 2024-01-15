def rotate_dice():
    num, nd = arr[x][y], d

    if bot > num:
        nd = (nd+1) % 4
    elif bot < num:
        nd = (nd+3) % 4
    return nd


def get_score():
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
    return num * len(visit)


def move_dice():
    nx, ny, nd = x + delta[d][0], y + delta[d][1], d
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        nd = (nd+2) % 4
        nx, ny = x + delta[nd][0], y + delta[nd][1]

    if not nd:
        ntop, nbot, nleft, nright, nup, ndown = left, right, bot, top, up, down
    elif nd == 1:
        ntop, nbot, nleft, nright, nup, ndown = up, down, left, right, bot, top
    elif nd == 2:
        ntop, nbot, nleft, nright, nup, ndown = right, left, top, bot, up, down
    else:
        ntop, nbot, nleft, nright, nup, ndown = down, up, left, right, top, bot

    return ntop, nbot, nleft, nright, nup, ndown, nx, ny, nd


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
x = y = d = ans = 0
top, bot, left, right, up, down = 1, 6, 4, 3, 2, 5
delta = ((0, 1), (1, 0), (0, -1), (-1, 0)) # E S W N

for _ in range(K):
    top, bot, left, right, up, down, x, y, d = move_dice()
    ans += get_score()
    d = rotate_dice()

print(ans)