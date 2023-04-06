import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
ans = 0

# 3, 4, 5
for i in range(N-1):
    for j in range(M-2):
        tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans = max(ans, tmp + arr[i+1][j], tmp + arr[i+1][j+1], tmp + arr[i+1][j+2], tmp - arr[i][j+2] + arr[i+1][j+1] + arr[i+1][j+2])
        tmp = arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
        ans = max(ans, tmp + arr[i][j], tmp + arr[i][j+1], tmp + arr[i][j+2], tmp - arr[i+1][j+2] + arr[i][j+1] + arr[i][j+2])

for i in range(N-2):
    for j in range(M-1):
        tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        ans = max(ans, tmp + arr[i][j+1], tmp + arr[i+1][j+1], tmp + arr[i+2][j+1], tmp - arr[i+2][j] + arr[i+1][j+1] + arr[i+2][j+1])
        tmp = arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
        ans = max(ans, tmp + arr[i][j], tmp + arr[i+1][j], tmp + arr[i+2][j], tmp - arr[i+2][j+1] + arr[i+1][j] + arr[i+2][j])
# 1
for i in range(N):
    tmp = arr[i][0] + arr[i][1] + arr[i][2] + arr[i][3]
    ans = max(ans, tmp)
    for j in range(1, M-3):
        tmp += arr[i][j+3] - arr[i][j-1]
        ans = max(ans, tmp)

for j in range(M):
    tmp = arr[0][j] + arr[1][j] + arr[2][j] + arr[3][j]
    ans = max(ans, tmp)
    for i in range(1, N-3):
        tmp += arr[i+3][j] - arr[i-1][j]
        ans = max(ans, tmp)

# 2
for i in range(N-1):
    for j in range(M-1):
        ans = max(ans, arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1])

print(ans)