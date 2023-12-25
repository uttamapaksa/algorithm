N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
wall = sum(1 for r in arr for c in r if c == 6)
cctv = [(arr[i][j], i, j) for i in range(N) for j in range(M) if 0 < arr[i][j] < 6]
cctv_len = len(cctv)
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # North, East, South, West

# return visible areas set
def observe(d, r, c):
    dr, dc = delta[d]
    nv = set()
    while 0 <= r < N and 0 <= c < M and arr[r][c] != 6:
        nv.add((r, c))
        r, c = r + dr, c + dc
    return nv

# visible areas per CCTV
areas = {i: [] for i in range(cctv_len)}
for i in range(cctv_len):
    n, r, c = cctv[i] # cctv_num, row, col
    area = [observe(d, r, c) for d in range(4)] # visible areas per direction
    if n == 1:
        for d in range(4):
            areas[i].append(area[d])
    elif n == 2:
        for d in range(2):
            areas[i].append(area[d] | area[d+2])
    elif n == 3:
        for d in range(4):
            areas[i].append(area[d] | area[(d+1)%4])
    elif n == 4:
        for d in range(4):
            areas[i].append(area[d] | area[(d+1)%4] | area[(d+2)%4])
    else:
        areas[i].append(area[0] | area[1] | area[2] | area[3])

# maximum visible areas count
maxv = 0
def sol(v, k):
    if k == cctv_len:
        global maxv
        maxv = max(maxv, len(v))
        return
    for nv in areas[k]:
        sol(v | nv, k+1)
sol(set(), 0)

print(N * M - wall - maxv)