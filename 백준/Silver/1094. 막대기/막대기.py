ans = 0
n = int(input())
for i in (64, 32, 16, 8, 4, 2, 1):
    if i & n: ans += 1
print(ans)