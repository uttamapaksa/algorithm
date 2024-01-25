N = int(input())
B = int(input())

ans = 0
s, e = 1, N*N

while s <= e:
    m = (s+e) // 2

    tmp = 0
    for i in range(1, N+1):
        tmp += min(m // i, N)

    if tmp >= B:
        ans = m
        e = m-1
    else:
        s = m+1

print(ans)