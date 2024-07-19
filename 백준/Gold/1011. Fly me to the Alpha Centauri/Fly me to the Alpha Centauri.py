ans = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    d = e-s
    r = int((d-1)**0.5)
    if d <= r*(r+1):
        ans.append(r*2)
    else:
        ans.append(r*2+1)
print("\n".join(map(str, ans)))