def Check5():
    for r in range(19):
        for c in range(19):
            if arr[r][c]:
                for di in range(4):
                    cnt = 1
                    nr = r + dr[di]
                    nc = c + dc[di]
                    if nr < 0 or nr >= 19 or nc < 0 or nc >= 19:
                        continue
                    while 0 <= nr < 19 and 0 <= nc < 19 and arr[r][c] == arr[nr][nc]:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= nr + dr[di] < 19 and 0 <= nc + dc[di] < 19 and arr[r][c] == arr[nr + dr[di]][
                                nc + dc[di]]:
                                break
                            if 0 <= r - dr[di] < 19 and 0 <= c - dc[di] < 19 and arr[r][c] == arr[r - dr[di]][
                                c - dc[di]]:
                                break
                            if di == 3:
                                return arr[r][c], r + 5, c - 3
                            else:
                                return arr[r][c], r + 1, c + 1
                        nr += dr[di]
                        nc += dc[di]
    return 0, -1, -1


dr = [0, 1, 1, 1]
dc = [1, 1, 0, -1]
arr = [list(map(int, input().split())) for _ in range(19)]
color, r, c = Check5()
if not color:
    print(color)
else:
    print(color)
    print(r, c)