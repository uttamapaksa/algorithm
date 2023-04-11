N, ans = int(input()), 0
x0, y0 = map(int, input().split())
x1, y1, = x0, y0
for i in range(N-1):
    x2, y2 = map(int, input().split())
    ans += (x1 + x2) * (y1 - y2)
    x1, y1 = x2, y2
ans += (x1 + x0) * (y1 - y0)
print(round(abs(ans/2), 1))