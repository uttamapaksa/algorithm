def find_and_delete_biggest_group():
    find = 0 # flag
    visit = set() # block_visit
    biggest_cnt = [0, 0, 0, 0] # block_cnt, rainbow_cnt, min_row, min_col
    biggest_group = [] # elements

    for i in range(N):
        for j in range(N):
            if arr[i][j] < 1 or (i, j) in visit: continue # only regular block
            num = arr[i][j]
            stack = [(i, j)]
            visit.add((i, j))
            r_visit = set() # rainbow_visit
            curr_cnt = [1, 0, i, j]
            curr_group = [(i, j)]

            # dfs
            while stack:
                r, c = stack.pop()
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= N: continue # index error
                    # same block 
                    if arr[nr][nc] == num:
                        if (nr, nc) not in visit:
                            stack.append((nr, nc))
                            visit.add((nr, nc))
                            block_cnt, rainbow_cnt, min_row, min_col = curr_cnt
                            curr_cnt = [block_cnt + 1, rainbow_cnt, *min((min_row, min_col), (nr, nc))] # update reference block
                            curr_group.append((nr, nc))
                    # rainbow block
                    elif not arr[nr][nc]:
                        if (nr, nc) not in r_visit:
                            stack.append((nr, nc))
                            r_visit.add((nr, nc))
                            block_cnt, rainbow_cnt, min_row, min_col = curr_cnt
                            curr_cnt = [block_cnt + 1, rainbow_cnt + 1, min_row, min_col]
                            curr_group.append((nr, nc))
            
            # upate biggest group
            if curr_cnt[0] > 1: # At least 2 blocks are required for a group
                if biggest_cnt < curr_cnt:
                    biggest_cnt = curr_cnt
                    biggest_group = curr_group
                find = 1

    # delete biggest group
    if find:
        for nr, nc in biggest_group:
            arr[nr][nc] = -2
        ans[0] += biggest_cnt[0] ** 2
    return find


def gravity():
    for j in range(N):
        for i in range(N-1, -1, -1):
            if arr[i][j] < 0: continue
            nr = i + 1
            while nr < N and arr[nr][j] == -2:
                arr[nr][j], arr[nr - 1][j] = arr[nr - 1][j], arr[nr][j]
                nr += 1


def rotate():
    # rotate the array counterclockwise
    new_arr = [*map(list, [*zip(*arr)])]
    for i in range(N):
        arr[i] = new_arr[N-i-1]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((1, 0), (0, -1), (-1, 0), (0, 1))
ans = [0]

while find_and_delete_biggest_group():
    gravity()
    rotate()
    gravity()

print(ans[0])