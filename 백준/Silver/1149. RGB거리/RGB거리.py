import sys; input = sys.stdin.readline

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]

for i in range(1, N):
    a, b, c = arr[i-1]
    arr[i] = [arr[i][0] + min(b, c), arr[i][1] + min(c, a), arr[i][2] + min(a, b)]

print(min(arr[N-1]))