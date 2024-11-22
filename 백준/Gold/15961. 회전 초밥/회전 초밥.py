import sys; input=sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = tuple(int(input()) for _ in range(n))
cnt = [0] * (d+1)
total = 0
for i in range(k):
    cnt[arr[i]] += 1
    if cnt[arr[i]] == 1:
        total += 1

ans = total
for i in range(n):
    ans = max(ans, total+(1 if cnt[c]==0 else 0))
    v = arr[i]
    cnt[v] -= 1
    if cnt[v] == 0:
        total -= 1
    v = arr[(k+i)%n]
    cnt[v] += 1
    if cnt[v] == 1:
        total += 1

print(ans)
