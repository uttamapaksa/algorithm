ans = 0
stack = []  # score, time
for _ in range(int(input())):
    ipt = tuple(map(int, input().split()))
    if not ipt[0]:
        if stack:
            if stack[-1][1] == 1:
                ans += stack.pop()[0]
                continue
            stack[-1][1] -= 1
    elif ipt[2] == 1:
        ans += ipt[1]
    else:
        stack.append([ipt[1], ipt[2]-1])
print(ans)