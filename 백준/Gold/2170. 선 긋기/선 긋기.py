N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
arr.sort(key=lambda x: (x[0], -x[1]))

ans = 0
s = e = -1000000001
for ns, ne in arr:
    if ns > s:
        if ns <= e:
            e = max(e, ne)
        else:
            ans += e - s
            s, e = ns, ne
ans += e - s

print(ans)