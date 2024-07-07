N = int(input())
arr = [*map(int, input().split())]
prev = [0, -1]  # idx, val
post = [0, -1]  # idx, val

ans = 0
cnt = 0
for i in range(N):
    if arr[i] != post[1]:
        if arr[i] == prev[1]:
            prev, post = [*post], [*prev]
            post[0] = i
        else:
            prev = [*post]
            post = [i, arr[i]]
            cnt = i - prev[0]
    cnt += 1
    ans = max(ans, cnt)

print(ans)