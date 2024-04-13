def rotate(arr, k):
    newArr = [[*row] for row in arr]
    if k == 0: # right
        pass
    elif k == 1: # left
        for r in range(N):
            for c in range(N):
                newArr[r][c] = arr[r][N-1-c]
    elif k == 2: # up
        for r in range(N):
            for c in range(N):
                newArr[r][c] = arr[N-1-c][r]
    else: # down
        for r in range(N):
            for c in range(N):
                newArr[r][c] = arr[c][r]
    return newArr


def merge(newArr):
    for r in range(N):
        prevIdx = prevVal = 0
        for c in range(N-1, -1, -1):
            if not newArr[r][c]: continue
            if prevVal == newArr[r][c]:
                newArr[r][prevIdx] *= 2
                newArr[r][c] = 0
                prevIdx = prevVal = 0
                continue
            prevIdx = c
            prevVal = newArr[r][c]


def move(newArr):
    for r in range(N):
        i = N-1
        for c in range(N-1, -1, -1):
            if newArr[r][c]:
                tmp = newArr[r][c]
                newArr[r][c] = 0
                newArr[r][i] = tmp
                i -= 1
        for c in range(i+1):
            newArr[r][c] = 0


def game(arr, k):
    if k == 5:
        global answer
        v = max(max(row) for row in arr)
        answer = max(answer, v)
        return

    for i in range(4):
        newArr = rotate(arr, i)
        merge(newArr)
        move(newArr)
        game(newArr, k+1)


N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
answer = 0

game(arr, 0)
print(answer)