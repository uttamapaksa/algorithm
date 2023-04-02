arr = input()
ans = 0
tmp = ''
plus = 1
for i in range(len(arr)):
    if arr[i].isdigit():
        tmp += arr[i]
    else:
        if plus:
            ans += int(tmp)
            if arr[i] == '-':
                plus = 0
        else:
            ans -= int(tmp)
        tmp = ''
if plus: ans += int(tmp)
else: ans -= int(tmp)
print(ans)