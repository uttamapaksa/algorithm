ans = ""
for _ in range(int(input())):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    stack = []
    for _, v in sorted(arr, key=lambda x: (-x[0], x[1])):
        while stack and stack[-1] > v:
            stack.pop()
        stack.append(v)
    ans += f"{len(stack)}\n"

print(ans)