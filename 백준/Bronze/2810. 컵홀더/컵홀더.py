n = int(input())
arr = [*input()]

ans = 0
isL = 0
i = 0
while i < n:
    if arr[i] == 'S':
        ans += 1
    else:
        isL = 1
        ans += 1
        i += 1
    i += 1

ans += isL

print(ans)