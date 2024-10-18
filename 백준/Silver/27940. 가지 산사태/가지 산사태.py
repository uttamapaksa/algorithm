flag, m, k = map(int, input().split())
for i in range(m):
    t, r = map(int, input().split())
    if not flag: continue
    k -= r
    if k < 0:
        flag = False
        print(i+1, 1)
if flag:
    print(-1)