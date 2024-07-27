def sol() -> str:
    u = 0
    for i in range(N-1):
        if '#' in arr[i]:
            u = i
            break
    for i in range(N-1, 0, -1):
        if '#' in arr[i]:
            uc = arr[u].count('#')
            dc = arr[i].count('#')
            if uc > dc: return 'DOWN'
            if uc < dc: return 'UP'
            for j in range(M-1):
                if arr[i][j] == '#':
                    for k in range(u, i+1):
                        if arr[k][j] == '.':
                            return 'LEFT'
                    return 'RIGHT'
    return ''

N, M = map(int,input().split())
arr = [[*input()] for _ in range(N)]
print(sol())