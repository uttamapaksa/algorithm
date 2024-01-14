def blizzard():
    nr, nc = SR, SC
    dr, dc = delta[d_map[d]]
    for _ in range(s):
        nr, nc = nr + dr, nc + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N: break
        arr[nr][nc] = 0


def moveBall():
    # create ball list
    global balls
    nr, nc, d, balls = SR, SC, 0, []
    for i in range(1, N):
        for _ in range(2):
            dr, dc = delta[d]
            for _ in range(i):
                nr, nc = nr + dr, nc + dc
                if arr[nr][nc]:
                    balls.append(arr[nr][nc])
            d = (d+1) % 4
    for j in range(N-2, -1, -1):
        if arr[0][j]:
            balls.append(arr[0][j])
    
    # calcuate cnt & num
    ballsCntNum = []
    for ball in balls:
        if ballsCntNum and ballsCntNum[-1][1] == ball:
            ballsCntNum[-1] = [ballsCntNum[-1][0] + 1, ball] # cnt, num
        else:
            ballsCntNum.append([1, ball])
    balls = ballsCntNum

    # explode balls
    explod = 1
    while explod:
        explod = 0
        stack = []
        for ball in balls:
            if stack and stack[-1][1] == ball[1]:
                stack[-1] = [stack[-1][0] + ball[0], ball[1]]
            else:
                stack.append(ball)
        for sta in stack: # cnt, num
            if sta[0] > 3: # explode
                ans[sta[1]] += sta[0]
                stack.remove(sta)
                explod = 1
        balls = stack


def transform():
    # transform balls
    global balls
    transBall, length = [], 0
    for ball in balls:
        if length >= MAX_LENGTH:
            break
        transBall.extend(ball)
        length += 2
    for _ in range(MAX_LENGTH - length):
        transBall.append(0)
    balls = transBall

    # update array
    nr, nc, d, j = SR, SC, 0, -1
    for i in range(1, N):
        for _ in range(2):
            dr, dc = delta[d]
            for _ in range(i):
                nr, nc, j = nr + dr, nc + dc, j + 1
                arr[nr][nc] = balls[j]
            d = (d+1) % 4
    for i in range(N-2, -1, -1):
        j += 1
        arr[0][i] = balls[j]


N, M = map(int, input().split())
SR = SC = N//2
MAX_LENGTH = N**2 - 1
arr = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int, input().split())) for _ in range(M)]
balls = []
delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
d_map = {0: 3, 1: 1, 2: 0, 3: 2}
ans = [0, 0, 0, 0]

for magic in magics:
    d, s = magic
    d -= 1
    blizzard()
    moveBall()
    transform()

print(sum(i * ans[i] for i in range(4)))