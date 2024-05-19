def cycle(r):
    global ans
    visit = set()
    u = r
    while u not in visit and u not in ans:
        visit.add(u)
        u = arr[u]
    if r == u:
        ans |= visit

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
ans = set()

for i in range(1, n+1):
    if i in ans: continue
    cycle(i)

print(len(ans))
print('\n'.join(map(str, sorted(ans))))