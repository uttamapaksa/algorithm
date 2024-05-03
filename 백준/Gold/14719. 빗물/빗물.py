N, M = map(int, input().split())
arr = [N+1] + [*map(int, input().split())] + [N+1]

dp1 = [0] * (M+2)
stack = [(N+1, 0)]
for i in range(1, M+1):
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
    for j in range(stack[-1][1]+1, i+1):
        dp1[j] = arr[i]
    stack.append((arr[i], i))

dp2 = [0] * (M+2)
stack = [(N+1, M+1)]
for i in range(M, 0, -1):
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
    for j in range(stack[-1][1]-1, i-1, -1):
        dp2[j] = arr[i]
    stack.append((arr[i], i))

answer = 0
for i in range(1, M+1):
    answer += min(dp1[i], dp2[i]) - arr[i]
print(answer)