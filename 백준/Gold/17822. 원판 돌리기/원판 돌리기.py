N, M, T = map(int, input().split())
arr = [[*map(int, input().split())] + [0] for _ in range(N)] # numbers + rotation index
remain = {(i, j) for i in range(N) for j in range(M)}


for _ in range(T):
    deleted = set()

    # rotate circles
    x, d, k = map(int, input().split())
    for i in range(x-1, N, x):
        if d:
            arr[i][M] = (arr[i][M] + M - k) % M
        else:
            arr[i][M] = (arr[i][M] + k) % M

    # remove adjacent numbers in a circle
    for r in range(N):
        for i in range(M):
            c1, c2 = i, (i+1) % M 
            if (r, c1) not in remain or (r, c2) not in remain:
                continue
            if arr[r][c1] == arr[r][c2]:
                deleted.add((r, c1))
                deleted.add((r, c2))

    # remove adjacent numbers in adjacent circles
    for r in range(0, N-1):
        i1, i2 = arr[r][M], arr[r+1][M] # rotation index
        for c in range(M):
            c1, c2 = (c + M - i1) % M,  (c + M - i2) % M
            if (r, c1) not in remain or (r+1, c2) not in remain:
                continue
            if arr[r][c1] == arr[r+1][c2]:
                deleted.add((r, c1))
                deleted.add((r+1, c2))

    # if there are not adjacent numbers, +1 or -1
    remain -= deleted
    if remain and not deleted:
        avg = sum(arr[i][j] for i, j in remain) / len(remain)
        for i, j in remain:
            if arr[i][j] > avg:
                arr[i][j] -= 1
            elif arr[i][j] < avg:
                arr[i][j] += 1

print(sum(arr[i][j] for i, j in remain))