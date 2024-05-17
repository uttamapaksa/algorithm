def solution(arr):
    n, m = len(arr), len(arr[0])
    arr = [[0] * (m+1)] + [[0] + row for row in arr]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j]:
                arr[i][j] = min(arr[i-1][j-1], arr[i-1][j], arr[i][j-1]) + 1
    
    ans = 0
    for row in arr:
        ans = max(ans, max(row))
    return ans ** 2