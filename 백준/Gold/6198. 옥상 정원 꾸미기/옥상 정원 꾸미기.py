n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
answer = 0

for i in range(n-1, -1, -1):
    w = 1
    while stack:
        if stack[-1][0] == arr[i]:
            nw = stack.pop()[1]
            w += nw
        elif stack[-1][0] < arr[i]:
            nw = stack.pop()[1]
            w += nw
            answer += nw
        else:
            break
    stack.append((arr[i], w))

print(answer)