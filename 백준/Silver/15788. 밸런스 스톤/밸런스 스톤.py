import sys; input=sys.stdin.readline

def sol():
    N = int(input())
    arr = tuple(tuple(map(int, input().split())) for _ in range(N))

    for r in range(N):
        for c in range(N):
            if not arr[r][c]:
                break
        else:
            continue
        break
    zr, zc = r, c

    full = sum(arr[0]) if zr else sum(arr[1])
    for r in range(N):
        if r == zr: continue
        if full != sum(arr[r]): return -1
    for c in range(N):
        if c == zc: continue
        if full != sum(arr[r][c] for r in range(N)): return -1
    if (zr != zc):
        if full != sum(arr[r][r] for r in range(N)): return -1
    if (zr + zc != N-1):
        if full != sum(arr[r][N-1-r] for r in range(N)): return -1

    blank = sum(arr[zr])
    if blank != sum(arr[r][zc] for r in range(N)): return -1
    if (zr == zc):
        if blank != sum(arr[r][r] for r in range(N)): return -1
    if (zr + zc == N-1):
        if blank != sum(arr[r][N-1-r] for r in range(N)): return -1

    if (full <= blank):
        return -1
    return full - blank 

print(sol())