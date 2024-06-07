n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

left = {}
for a in A:
    for b in B:
        left[a+b] = left.get(a+b, 0) + 1
ans = 0
for c in C:
    for d in D:
        ans += left.get(-c-d, 0)
        
print(ans)