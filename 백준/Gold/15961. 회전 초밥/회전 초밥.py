n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)] * 2
curr = set()
cnt = [0] * (d+1)
for v in arr[:k]:
    curr.add(v)
    cnt[v] += 1

ans = len(curr)
for i in range(n):
    if c not in curr:
        ans = max(ans, len(curr) + 1)
    else:
        ans = max(ans, len(curr))
    v = arr[i]
    cnt[v] -= 1
    if cnt[v] == 0:
        curr.remove(v)
    v = arr[k+i]
    cnt[v] += 1
    if cnt[v] == 1:
        curr.add(v)

print(ans)