N =  int(input())
arr = [[-1] * (N+2)] + [[-1] + [0] * (N) + [-1] for _ in range(N)] + [[-1] * (N+2)] # -1 to prevent index error
like = {a: set(b) for _ in range(N**2) for a, *b in [map(int, input().split())]}


for student in like:
    blank = [0, 0, N+1, N+1] # blank to move (adj, empty, row, col)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j]: continue

            tmp = [0, 0, i, j]
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if arr[ni][nj] in like[student]:
                    tmp[0] -= 1 # minus for max heap
                elif not arr[ni][nj]:
                    tmp[1] -= 1 # minus for max heap
            blank = min(blank, tmp)

    arr[blank[2]][blank[3]] = student


ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        adj = 0
        for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
             if arr[ni][nj] in like[arr[i][j]]:
                adj += 1
        if adj:
            ans += 10 ** (adj-1)
print(ans)