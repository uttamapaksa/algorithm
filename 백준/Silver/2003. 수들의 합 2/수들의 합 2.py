N, M = map(int, input().split())
arr = tuple(map(int, input().split()))
res = i = j = 0
cur = arr[j]

while j < N-1:
    if cur <= M:
        if cur == M:
            res += 1
        j += 1
        cur += arr[j]
    else:
        i += 1
        cur -= arr[i-1]
while i <= j:
    if cur == M:
        res += 1
    i += 1
    cur -= arr[i-1]

print(res)