from itertools import combinations

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def turn(c1, c2, c3, k, v):
    if k == N:
        global ans
        ans = max(ans, v)
        return
    kill_set = set((kill(c1, k), kill(c2, k), kill(c3, k)))
    for x, y in kill_set:
        if x != 20:
            arr[x][y] = 0
            v += 1
    turn(c1, c2, c3, k+1, v)
    for x, y in kill_set:
        if x != 20:
            arr[x][y] = 1
            v -= 1


def kill(c, k):
    for w in range(D):
        nr, nc = N-k-1, c - w
        # first postion
        if nc >= 0 and arr[nr][nc]: 
            return nr, nc
        # go up-right
        for _ in range(w): 
            nr, nc = nr - 1, nc + 1
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                return nr, nc
        # go down-right
        for _ in range(w):
            nr, nc = nr + 1, nc + 1
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                return nr, nc
    return 20, 20


for comb in combinations(range(M), 3):
    c1, c2, c3 = comb
    turn(c1, c2, c3, 0, 0)

print(ans)