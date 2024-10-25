def sol():
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not arr[r][c]:
                break
        else:
            continue
        break
    zr, zc = r, c

    sums = set()
    for r in range(N):
        if r == zr: continue
        sums.add(sum(arr[r]))
    for c in range(N):
        if c == zc: continue
        sums.add(sum(arr[r][c] for r in range(N)))
    if (zr != zc):
        sums.add(sum(arr[r][r] for r in range(N)))
    if (zr + zc != N-1):
        sums.add(sum(arr[r][N-1-r] for r in range(N)))
    if len(sums) > 1:
        return -1
    sums = tuple(sums)[0]

    zsums = set()
    zsums.add(sum(arr[zr]))
    zsums.add(sum(arr[r][zc] for r in range(N)))
    if (zr == zc):
        zsums.add(sum(arr[r][r] for r in range(N)))
    if (zr + zc == N-1):
        zsums.add(sum(arr[r][N-1-r] for r in range(N)))
    if len(zsums) > 1:
        return -1
    zsums = tuple(zsums)[0]

    if (sums <= zsums):
        return - 1
    return sums - zsums 

print(sol())