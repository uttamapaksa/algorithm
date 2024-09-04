def sol():
    for i in range(N):
        # row
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == '.':
                cnt = 0
                continue
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return arr[i][j]
        # col
        cnt = 1
        for j in range(1, N):
            if arr[j][i] == '.':
                cnt = 0
                continue
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return arr[j][i]
    # rigth dia
    for i in range(N-2):
        nr, nc, cnt = i, 0, 1
        while True:
            r, c = nr, nc
            nr, nc = r+1, c+1
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if arr[nr][nc] == '.':
                cnt = 0
                continue
            if arr[nr][nc] == arr[r][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return arr[nr][nc]
        nr, nc, cnt = 0, i, 1
        while True:
            r, c = nr, nc
            nr, nc = r+1, c+1
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if arr[nr][nc] == '.':
                cnt = 0
                continue
            if arr[nr][nc] == arr[r][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return arr[nr][nc]
    # left dia
    for i in range(N-2):
        nr, nc, cnt = i, N-1, 1
        while True:
            r, c = nr, nc
            nr, nc = r+1, c-1
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if arr[nr][nc] == '.':
                cnt = 0
                continue
            if arr[nr][nc] == arr[r][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return arr[nr][nc]
        nr, nc, cnt = 0, i+2, 0
        while True:
            r, c = nr, nc
            nr, nc = r+1, c-1
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break
            if arr[nr][nc] == '.':
                cnt = 0
                continue
            if arr[nr][nc] == arr[r][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt == 3:
                return arr[nr][nc]

    return 'ongoing'


N = int(input())
arr = [[*input()] for _ in range(N)]
print(sol())