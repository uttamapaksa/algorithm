n, k = map(int, input().split())
arr = [0] + [*map(int, input().split())]
for i in range(2, n+1):
    arr[i] += arr[i-1]

sums = {}
ans = 0
for i in range(n+1):
    v = arr[i]
    if v-k in sums:
       ans += sums[v-k]
    sums[v] = sums.get(v, 0) + 1

print(ans)