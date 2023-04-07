import sys
input = sys.stdin.readline

# 이전 합들을 배열에 저장
N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for j in range(1, N):
        arr[i][j] += arr[i][j-1]
for j in range(N):
    for i in range(1, N):
        arr[i][j] += arr[i-1][j]

# 선택된 합 - 선택 안 된 합
for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2, ans = r1 - 1, c1 - 1, r2 - 1, c2 - 1, 0
    if not r1 and not c1:
        print(arr[r2][c2])
    elif not r1:
        print(arr[r2][c2] - arr[r2][c1-1])
    elif not c1:
        print(arr[r2][c2] - arr[r1-1][c2])
    else:
        print(arr[r2][c2] - arr[r1-1][c2] - arr[r2][c1-1] + arr[r1-1][c1-1])
