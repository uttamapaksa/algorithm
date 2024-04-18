from collections import deque

# move
def moveRed(r1, r2, b1, b2, d):
    di, dj = delta[d]
    ci, cj = r1, r2
    while True:
        ni, nj = ci + di, cj + dj
        if arr[ni][nj] == 2:
            return 0, 0
        if arr[ni][nj] == 1 or (ni == b1 and nj == b2):
            break
        ci, cj = ni, nj

    return ci, cj

def moveBlue(r1, r2, b1, b2, d):
    di, dj = delta[d]
    ci, cj = b1, b2
    while True:
        ni, nj = ci + di, cj + dj
        if arr[ni][nj] == 2:
            return 0, 0
        if arr[ni][nj] == 1 or (ni == r1 and nj == r2):
            break
        ci, cj = ni, nj

    return ci, cj


# static
convert = {".": 0, "#": 1, "R": 0, "B": 0, "O": 2}
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
r1 = r2 = b1 = b2 = 0
answer = -1

# input
N, M = map(int, input().split())
arr = [[*input()] for _ in range(N)]
visit = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# convert to Integer
for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            r1, r2 = i, j
        elif arr[i][j] == "B":
            b1, b2 = i, j
        arr[i][j] = convert[arr[i][j]]

# bfs
queue = deque([(r1, r2, b1, b2, 1)])
while queue:
    # brute force
    r1, r2, b1, b2, cnt = queue.popleft()
    # over
    if cnt == 11:
        continue
    # up
    if r1 <= b1:
        nr1, nr2 = moveRed(r1, r2, b1, b2, 0)
        nb1, nb2 = moveBlue(nr1, nr2, b1, b2, 0)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    else:
        nb1, nb2 = moveBlue(r1, r2, b1, b2, 0)
        nr1, nr2 = moveRed(r1, r2, nb1, nb2, 0)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    # down
    if r1 >= b1:
        nr1, nr2 = moveRed(r1, r2, b1, b2, 1)
        nb1, nb2 = moveBlue(nr1, nr2, b1, b2, 1)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    else:
        nb1, nb2 = moveBlue(r1, r2, b1, b2, 1)
        nr1, nr2 = moveRed(r1, r2, nb1, nb2, 1)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    # left
    if r2 <= b2:
        nr1, nr2 = moveRed(r1, r2, b1, b2, 2)
        nb1, nb2 = moveBlue(nr1, nr2, b1, b2, 2)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    else:
        nb1, nb2 = moveBlue(r1, r2, b1, b2, 2)
        nr1, nr2 = moveRed(r1, r2, nb1, nb2, 2)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    # right
    if r2 >= b2:
        nr1, nr2 = moveRed(r1, r2, b1, b2, 3)
        nb1, nb2 = moveBlue(nr1, nr2, b1, b2, 3)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))
    else:
        nb1, nb2 = moveBlue(r1, r2, b1, b2, 3)
        nr1, nr2 = moveRed(r1, r2, nb1, nb2, 3)
        if not nr1 and nb1: answer = cnt; break
        if not visit[nr1][nr2][nb1][nb2]:
            visit[nr1][nr2][nb1][nb2] = 1
            queue.append((nr1, nr2, nb1, nb2, cnt+1))

print(answer)