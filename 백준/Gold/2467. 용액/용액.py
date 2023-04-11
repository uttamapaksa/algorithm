import sys; input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
mins = 3000000000
ans = [0, 0]

end = 0
for i in range(N - 1):
    now = arr[i]
    s, e = i + 1, N-1
    while s <= e:
        mid = (s + e) // 2
        new = arr[mid]
        value = now + new
        if abs(value) >= mins:
            if now > 0:
                e = mid - 1
            else:
                if abs(now) > abs(new):
                    s = mid + 1
                else:
                    e = mid - 1
        elif mins > abs(value) > 0:
            mins = abs(value)
            ans = [now, new]
            if now > 0:
                e = mid - 1
            else:
                if abs(now) > abs(new):
                    s = mid + 1
                else:
                    e = mid - 1
        else:
            end = 1
            mins = 0
            ans = [now, new]
            break
    if end: break

print(*ans)