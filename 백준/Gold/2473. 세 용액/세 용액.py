import sys; input = sys.stdin.readline

N = int(input())
arr = [*map(int, input().split())]
arr.sort()
mins = 3000000000

end = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        now = arr[i] + arr[j]
        s, e = j + 1, N - 1
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
                ans = [arr[i], arr[j], new]
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
                ans = [arr[i], arr[j], new]
                break
        if end: break
    if end: break

print(*ans)