N, M = map(int, input().split())
A = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: (x[1]))

ans = 0
fe = rs = re = -1  # 순방향 e, 역방향 s, 역방향 e
for s, e, in A:
    if s < e:
        fe = max(e, fe)
    else:
        if e <= rs:
            rs = max(s, rs)
        else:
            ans += 2 * (rs - re)
            rs, re = s, e
ans += 2 * (rs - re)
fe = max(rs, fe)
if fe < M:
    ans += M
else:
    ans += fe + fe - M

print(ans)