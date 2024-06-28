def dnq(r, c, w):
    if w == 1:
        return arr[r][c]
    if w == 2:
        return sorted((arr[r][c], arr[r+1][c], arr[r][c+1], arr[r+1][c+1]))[1]
    w >>= 1
    return sorted((dnq(r, c, w), dnq(r+w, c, w), dnq(r, c+w, w), dnq(r+w, c+w, w)))[1]

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
print(dnq(0, 0, N))