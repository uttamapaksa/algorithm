N = int(input())
arr = [*map(int, input().split())]
answer = [0] * N

stack = [(1000000001, -1)]
for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        idx = stack.pop()[1]
        answer[idx] = stack[-1][1] + 1
    stack.append((arr[i], i))

for _ in range(len(stack) - 1):
    idx = stack.pop()[1]
    answer[idx] = stack[-1][1] + 1

print(*answer)