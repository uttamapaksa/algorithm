n = int(input())
arr = [*map(int, input().split())]
left = [1] * n
right = [1] * n

for i in range(n):
    tmp = 0
    for j in range(0, i):
        if arr[i] <= arr[j]:
            continue
        else:
            left[i] = max(left[i], left[j]+1)

for i in range(n-1, -1, -1):
    tmp = 0
    for j in range(n-1, i, -1):
        if arr[i] <= arr[j]:
            continue
        else:
            right[i] = max(right[i], right[j]+1)

ans = 0
for i in range(n):
   ans = max(ans, left[i] + right[i])

print(ans - 1)
