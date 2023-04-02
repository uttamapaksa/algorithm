n = int(input())
arr = [*map(int, input().split())]
arr2 = sorted(arr)
ans = {}

k = 0
for i in range(n):
    if arr2[i] not in ans:
        ans[arr2[i]] = k
        k += 1

for i in arr:
    print(ans[i], end=' ')