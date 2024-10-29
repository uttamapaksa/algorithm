_ = input()
ans = sum(map(int, input().split()))
i = 0
for a in sorted(map(int, input().split())):
    ans += a * i
    i += 1
print(ans)