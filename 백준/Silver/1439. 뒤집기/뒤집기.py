N = input()
s = N[0]
ans = 0

for i in N:
    if i != s:
        ans += 1
        s = i
        
print(ans // 2 + ans % 2)