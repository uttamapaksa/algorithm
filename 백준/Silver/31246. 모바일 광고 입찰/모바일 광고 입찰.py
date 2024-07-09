N, K = map(int, input().split())

win = 0
cnt = {0: 0}
for _ in range(N):
    a, b = map(int, input().split())
    if a >= b:
        win += 1
    else:
        cnt[b-a] = cnt.get(b-a, 0) + 1

for x, c in sorted(cnt.items()):
    win += c
    if win >= K:
        print(x)
        break