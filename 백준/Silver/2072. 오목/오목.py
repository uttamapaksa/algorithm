board = [[0] * 20 for _ in range(20)]
N = int(input())

color = 3
for i in range(1, N+1):
    color ^= 1
    r, c = map(int, input().split())
    board[r][c] = color

    for dr1, dc1, dr2, dc2 in ((-1,-1,1,1), (-1,1,1,-1), (0,-1,0,1), (-1,0,1,0)):
        curr = 1
        nr, nc = r, c
        while 1:
            nr, nc = nr + dr1, nc + dc1
            if 1 > nr or nr >= 20 or 1 > nc or nc >= 20 or board[nr][nc] != color: break
            curr += 1
        nr, nc = r, c
        while 1:
            nr, nc = nr + dr2, nc + dc2
            if 1 > nr or nr >= 20 or 1 > nc or nc >= 20 or board[nr][nc] != color: break
            curr += 1
        
        if curr == 5:
            print(i)
            exit()

print(-1)