def dnq(r, c, w):
    if not w:
        return arr[r][c]
    w //= 2
    return sorted((dnq(r, c, w), dnq(r+w, c, w), dnq(r, c+w, w), dnq(r+w, c+w, w)))[2]


N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
print(dnq(0, 0, N))