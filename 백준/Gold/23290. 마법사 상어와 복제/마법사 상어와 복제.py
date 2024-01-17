def fish_move():
    global fish

    new_fish = {}
    for x, y in fish:
        cnt = fish[(x,y)]
        for d in range(8):
            if not cnt[d]: continue
            nd = d
            for _ in range(8):
                dx, dy = fish_delta[nd]
                nx, ny = x+dx, y+dy
                if 0<=nx<4 and 0<=ny<4 and (nx,ny)!=(sx,sy) and not smell_cnt[nx][ny]:
                    if (nx,ny) in new_fish:
                        new_fish[(nx,ny)][nd] += cnt[d]
                    else:
                        tmp = [0] * 8
                        tmp[nd] = cnt[d]
                        new_fish[(nx,ny)] = tmp
                    break
                nd = (nd+7) % 8
            else:
                if (x,y) in new_fish:
                    new_fish[(x,y)][nd] += cnt[d]
                else:
                    tmp = [0] * 8
                    tmp[nd] = cnt[d]
                    new_fish[(x,y)] = tmp

    for x, y in fish:
        fish_cnt[x][y] = 0
    for x, y in new_fish:
        fish_cnt[x][y] = sum(new_fish[(x,y)])
    fish = new_fish
    

def shark_move():
    global sx, sy

    def dfs(sx, sy, f, v, k):
        nonlocal max_visit, max_fish

        if k == 3:
            if f > max_fish:
                max_fish = f
                max_visit = [e for e in v]
            return
        for dx, dy in shark_delta:
            nx, ny = sx+dx, sy+dy
            if 0<=nx<4 and 0<=ny<4:
                if (nx,ny) in v:
                    dfs(nx, ny, f, v+[(nx,ny)], k+1) # ate already
                else:
                    dfs(nx, ny, f+fish_cnt[nx][ny], v+[(nx,ny)], k+1)
    
    max_fish, max_visit = -1, []
    dfs(sx, sy, 0, [], 0)
    sx, sy = max_visit[2]
    for x, y in max_visit:
        if fish_cnt[x][y]:
            del fish[(x,y)]
            fish_cnt[x][y] = 0
            smell_cnt[x][y] = 3
        

def smell_disappear():
    for i in range(4):
        for j in range(4):
            if smell_cnt[i][j]:
                smell_cnt[i][j] -= 1  


def duplicate_fish():
    global copied_fish

    for x, y in copied_fish:
        cnt = copied_fish[(x,y)]
        if (x,y) in fish:
            for d in range(8):
                fish[(x,y)][d] += cnt[d]
        else:
            fish[(x,y)] = cnt
        fish_cnt[x][y] += sum(cnt)
    copied_fish = fish.copy()


M, S = map(int, input().split())
fish = {}
for _ in range(M):
    x, y, d = map(lambda x: x-1, map(int, input().split()))
    if (x,y) in fish:
        fish[(x,y)][d] += 1
    else:
        tmp = [0] * 8
        tmp[d] = 1
        fish[(x,y)] = tmp
copied_fish = fish.copy()
sx, sy = map(lambda x: x-1, map(int, input().split()))
fish_cnt = [[0] * 4 for _ in range(4)]
smell_cnt = [[0] * 4 for _ in range(4)]
fish_delta = ((0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1))
shark_delta = ((-1,0), (0,-1), (1,0), (0,1))

for _ in range(S):
    fish_move()
    shark_move()
    smell_disappear()
    duplicate_fish()

ans = sum(sum(row) for row in fish_cnt)
print(ans)