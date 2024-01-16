def smell_disappear():
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if not smell[i][j][1]:
                    smell[i][j] = 0


def spray_smell():
    for shark in sharks:
        r, c, _ = sharks[shark]
        smell[r][c] = [shark, K]


def move_shark():
    global sharks

    new_shark_idx = {} # new sharks index
    for shark in sharks:
        r, c, d = sharks[shark]
        # blank
        for nd in priority_dir[shark][d]:
            nr, nc = r + dr[nd], c + dc[nd]
            if 0 <= nr < N and  0 <= nc < N and not smell[nr][nc]:
                if (nr, nc) in new_shark_idx:
                    new_shark_idx[(nr, nc)] = min(new_shark_idx[(nr, nc)], [shark, nd])
                else:
                    new_shark_idx[(nr, nc)] = [shark, nd]
                break
        # own smell
        else:
            for nd in priority_dir[shark][d]:
                nr, nc = r + dr[nd], c + dc[nd]
                if 0 <= nr < N and  0 <= nc < N and smell[nr][nc] and smell[nr][nc][0] == shark:
                    if (nr, nc) in new_shark_idx:
                        new_shark_idx[(nr, nc)] = min(new_shark_idx[(nr, nc)], [shark, nd])
                    else:
                        new_shark_idx[(nr, nc)] = [shark, nd]
                    break
    
    sharks = {new_shark_idx[(r, c)][0]: [r, c, new_shark_idx[(r, c)][1]] for r, c in new_shark_idx} # update sharks
    if len(sharks) == 1:
        return 1
    
    smell_disappear()
    spray_smell()


def adult_shark():
    time = 1
    while time < 1001:
        if move_shark():
            return time
        time += 1

    return -1


N, M, K = map(int, input().split())
smell = [list(map(int, input().split())) for _ in range(N)]
start_dir = [0] + list(map(int, input().split()))
priority_dir = {i: [0] + [list(map(int, input().split())) for _ in range(4)] for i in range(1, M+1)}
sharks = {smell[i][j]: [i, j, start_dir[smell[i][j]]] for i in range(N) for j in range(N) if smell[i][j]}
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

spray_smell()
print(adult_shark())