import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    tmp = [*map(int, input().split())]
    for i in range(1, N):
        tmp[i] += tmp[i-1]
    arr.append(tmp)
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2, ans = x1 - 1, y1 - 1, x2 - 1, y2 - 1, 0
    if not y1:
        for i in range(x1, x2 + 1):
            ans += arr[i][y2]
    else:
        for i in range(x1, x2 + 1):
            ans += arr[i][y2] - arr[i][y1 - 1]
    print(ans)