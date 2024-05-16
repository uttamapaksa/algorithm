def dfs(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'P':
                stack = [(i, j, True)]
                while stack:
                    r, c, go = stack.pop()
                    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
                        if arr[nr][nc] == 'X' or (nr == i and nc == j): continue
                        if arr[nr][nc] == 'P':
                            return 0
                        if go:
                            stack.append((nr, nc, False))
    return 1


def solution(places):
    ans = []
    for place in places:
        ans.append(dfs(place))
    
    return ans