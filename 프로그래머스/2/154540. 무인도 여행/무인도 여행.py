def solution(maps):
    arr = [[*row] for row in maps]
    n, m = len(arr), len(arr[0])
    
    ans = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'X': continue
            curr = int(arr[i][j])
            stack = [(i, j)]
            arr[i][j] = 'X'
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or arr[nr][nc] == 'X': continue
                    curr += int(arr[nr][nc])
                    stack.append((nr, nc))
                    arr[nr][nc] = 'X'
            ans.append(curr)
            
    if not ans:
        return [-1]
    return sorted(ans)
