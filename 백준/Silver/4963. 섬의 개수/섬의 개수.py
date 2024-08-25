import sys; input=sys.stdin.readline
while 1:
    w, h = map(int, input().split())
    if not w+h: break
    arr = [[*map(int, input().split())] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if not arr[i][j]: continue
            ans += 1
            arr[i][j] = 0
            stack = [(i, j)]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r+1,c+1),(r+1,c),(r+1,c-1),(r,c+1),(r,c-1),(r-1,c+1),(r-1,c),(r-1,c-1)):
                    if nr < 0 or nr >= h or nc < 0 or nc >= w or not arr[nr][nc]: continue
                    arr[nr][nc] = 0
                    stack.append((nr,nc))
    print(ans)