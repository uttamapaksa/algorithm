def make_cnt_table():
    global cnt_set_num
    for i in range(N):
        for j in range(M):
            if not arr[i][j] and not cnt[i][j]:
                cnt_set_num += 1
                stack = [(i,j)]
                visit = {(i,j)}
                cnt[i][j] = cnt_set_num

                while stack:
                    r, c = stack.pop()
                    for dr, dc in delta:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<N and 0<=nc<M and not arr[nr][nc] and (nr,nc) not in visit:
                            stack.append((nr,nc))
                            visit.add((nr,nc))
                            cnt[nr][nc] = cnt_set_num

                cnt_set[cnt_set_num] = len(visit)


def update_movable_cnt():
    for r in range(N):
        for c in range(M):
            if arr[r][c]:

                adj_set = set()
                for dr, dc in delta:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<N and 0<=nc<M and cnt[nr][nc]:
                        adj_set.add(cnt[nr][nc])

                movable_cnt = 1
                for num in adj_set:
                    movable_cnt += cnt_set[num]
                arr[r][c] = movable_cnt % 10


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
cnt = [[0] * M for _ in range(N)]
cnt_set = {}
cnt_set_num = 0
delta = ((-1,0),(1,0),(0,-1),(0,1))
make_cnt_table()
update_movable_cnt()

for l in arr:
    print(*l, sep='')