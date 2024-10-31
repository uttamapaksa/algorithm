from math import ceil

n, d = map(int, input().split())
par = [0] * (n+1)
for c in map(int, input().split()):
    par[c] += 1
    
ans = 0
for c in par:
    if c > d:
        ans += ceil((c-d)/(d-1))
print(ans)