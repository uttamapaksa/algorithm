N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
for i in range(1, N):
    arr[i][0] += arr[i-1][0]
    arr[i][-1] += arr[i-1][-1]
for i in range(2, N):
    for j in range(1, i):
        arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[-1]))