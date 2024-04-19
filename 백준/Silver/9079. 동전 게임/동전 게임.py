def isVisited(k):
    currVisit = f"{k}"
    for i in range(3):
        for j in range(3):
            currVisit += f"{arr[i][j]}"
    if currVisit not in visit:
        visit.add(currVisit)
        return 0
    return 1

def validate():
    a = arr[0][0]
    for i in range(3):
        for j in range(3):
            if arr[i][j] != a:
                return 0
    return 1

def dfs(k):
    global ans
    if k >= ans:
        return
    if isVisited(k):
        return
    if validate():
        ans = min(ans, k)
        return
    if k == 8:
        return

    # row
    for r in range(3):
        for c in range(3):
            arr[r][c] ^= 1
        dfs(k+1)
        for c in range(3):
            arr[r][c] ^= 1
    # col
    for c in range(3):
        for r in range(3):
            arr[r][c] ^= 1
        dfs(k+1)
        for r in range(3):
            arr[r][c] ^= 1
    # diagonal
    for i in range(3):
        arr[i][i] ^= 1
    dfs(k+1)
    for i in range(3):
        arr[i][i] ^= 1
    for i in range(3):
        arr[i][2-i] ^= 1
    dfs(k+1)
    for i in range(3):
        arr[i][2-i] ^= 1

# static
convert = {"H": 0, "T": 1}

# input
tc = int(input())
for _ in range(tc):
    arr = [[convert[e] for e in input().split()] for _ in range(3)]
    visit = set()

    ans = 9
    dfs(0)
    print(ans if ans != 9 else -1)