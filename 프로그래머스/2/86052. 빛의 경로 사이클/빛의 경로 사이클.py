delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # north, east, south, west
strdelta = {'S': 0, 'L': 3, 'R': 1}

def solution(grid):
    n = len(grid); m = len(grid[0])
    visit = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    answer = []
    
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visit[i][j][k]: continue
                start = (i, j, k)  # start
                ci, cj, ck = start  # curr
                visit[ci][cj][ck] = 1  # visit
                cnt = 0  # cnt
                while True:
                    ni, nj = (ci + delta[ck][0]) % n, (cj + delta[ck][1]) % m  # next
                    nk = (ck + strdelta[grid[ni][nj]]) % 4
                    cnt += 1
                    if (ni, nj, nk) == start:
                        answer.append(cnt)
                        break
                    if visit[ni][nj][nk]:
                        break
                    ci, cj, ck = ni, nj, nk
                    visit[ci][cj][ck] = 1
    
    answer.sort()
    return answer