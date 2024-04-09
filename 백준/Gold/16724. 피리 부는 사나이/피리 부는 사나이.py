def find(x, y):
    if P[x][y] != [x, y]:
        P[x][y] = find(*P[x][y])
    return P[x][y]

def union(x1, y1, x2, y2):
    a1, b1 = find(x1, y1)
    a2, b2 = find(x2, y2)
    if a1 < a2 or a1 == a2 and b1 < b2:
        P[a2][b2] = [a1, b1]
    else:
        P[a1][b1] = [a2, b2]

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
dirs = {"R": 0, "D": 1, "L": 2, "U": 3}
N, M = map(int, input().split())
P = [[[i, j] for j in range(M)] for i in range(N)]
arr = [[dirs[char] for char in input()] for _ in range(N)]

for r in range(N):
    for c in range(M):
        dr, dc = delta[arr[r][c]]
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            union(r, c, nr, nc)
            
for r in range(N):
    for c in range(M):
        find(r, c);

ansset = set()
for r in P:
    for c in r:
        ansset.add(tuple(c))
        
print(len(ansset))