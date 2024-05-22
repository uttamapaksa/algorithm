from collections import deque


def startPoint():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    return i, j, k


# sol
def bfs():
    sl, sr, sc = startPoint() 
    q = deque([(sl, sr, sc, 1)])
    arr[sl][sr][sc] = '#'
    while q:
        cl, cr, cc, cnt = q.popleft()
        for nl, nr, nc in ((cl+1, cr, cc), (cl-1, cr, cc), (cl, cr+1, cc), (cl, cr-1, cc), (cl, cr, cc+1), (cl, cr, cc-1)):
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and not arr[nl][nr][nc] == '#':
                if arr[nl][nr][nc] == 'E':
                    ans.append(f'Escaped in {cnt} minute(s).')
                    return
                q.append((nl, nr, nc, cnt+1))
                arr[nl][nr][nc] = '#'
    ans.append('Trapped!')


# input
ans = []
while True:
    L, R, C = map(int, input().split())
    if not sum((L, R, C)): break

    arr = []
    for _ in range(L):
        floor = [[*input()] for _ in range(R)]
        arr.append(floor)
        _ = input()
    
    bfs()
print("\n".join(ans))