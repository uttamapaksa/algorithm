n, k = map(int, input().split())
pre = ans = 0

for x, t, s in sorted(tuple(map(int, input().split())) for _ in range(k)):
    ans += x - pre
    pre = x
    if ans <= s:
        ans = s
    else:
        tmp = ans - s
        if (tmp // t) & 1:
            ans += (t - tmp % t)
ans += n - pre

print(ans)