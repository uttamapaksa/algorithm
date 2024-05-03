n = int(input())
arr = [*map(int, input().split())]
memo = {}

for i in range(n-1):
    v1 = arr[i]
    for j in range(i+1, n):
        v2 = v1 + arr[j]
        if v2 in memo:
            memo[v2].append((i, j))
        else:
            memo[v2] = [(i, j)]

ans = 0
for i in range(n):
    v1 = arr[i]
    if v1 in memo:
        for i2, i3 in memo[v1]:
            if i != i2 and i != i3:
                ans += 1
                break

print(ans)