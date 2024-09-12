N, L = map(int, input().split())
for v in sorted(map(int, input().split())):
    if L >= v: L += 1
    else: break
print(L)