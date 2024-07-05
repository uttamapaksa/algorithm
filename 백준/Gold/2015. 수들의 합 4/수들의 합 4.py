n, k = map(int, input().split())
arr = [0] + [*map(int, input().split())]
for i in range(2, n+1):
    arr[i] += arr[i-1]

ans = 0
sums = {}
for v in arr:
    ans += sums.get(v-k, 0)
    sums[v] = sums.get(v, 0) + 1

print(ans)