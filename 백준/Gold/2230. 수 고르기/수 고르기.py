N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

ans = float('inf')
i, j = 0, 1
while j < N:
    if i == j:
        j += 1
        continue
    diff = arr[j] - arr[i]
    if diff > M:
        ans = min(ans, diff)
        i += 1
    elif diff == M:
        ans = M
        break
    else:
        j += 1

print(ans)