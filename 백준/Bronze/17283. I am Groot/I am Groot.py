L = int(input())
R = int(input())
C = 1

ans = 0
while 1:
    L = int(L * R / 100)
    C <<= 1
    if L <= 5:
        break
    ans += L * C

print(ans)