def teenage_shark(arr, sr, sc, sd, v): # array, shark row, shark col, shark direction, sum of eaten fish
    # update max value
    global ans; ans = max(ans, v)

    # copy arr, eat fish, make fish list
    arr = [[*r] for r in arr]
    arr[sr][sc] = [0, 0]
    fish = {arr[i][j][0]: [arr[i][j][1], i, j] for i in range(4) for j in range(4) if arr[i][j][0]} # num: dir, row, col

    # move fish
    for num in range(1, 17):
        if num not in fish: continue
        d, r, c = fish[num] # dir, row, col
        for _ in range(8):
            dr, dc =  delta[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (sr, sc):
                # move to blank
                if not arr[nr][nc][0]:
                    arr[nr][nc], arr[r][c] = [num, d], [0, 0] # swap arr
                    fish[num] = [d, nr, nc] # swap fish
                # move to other fish
                else:
                    swap_num = arr[nr][nc][0] # fish numbers to swap
                    arr[nr][nc], arr[r][c] = [num, d], [swap_num, fish[swap_num][0]] # swap arr
                    fish[num], fish[swap_num] = [d, nr, nc], [fish[swap_num][0], r, c] # swap fish
                break
            d = (d+1) % 8

    # move shark
    nr, nc = sr, sc
    dr, dc = delta[sd]
    for _ in range(3): # maximum moving distance = 3
        nr, nc = nr + dr, nc + dc
        if 0 <= nr < 4 and 0 <= nc < 4 and arr[nr][nc][0]:
            num, nd = arr[nr][nc]
            teenage_shark(arr, nr, nc, nd, v + num)


delta = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
arr = [[[tmp[j*2], tmp[j*2+1]-1] for j in range(4)]  for _ in range(4) for tmp in [list(map(int, input().split()))]] # num, dir-1
ans, sd = arr[0][0]

teenage_shark(arr, 0, 0, sd, ans)
print(ans)