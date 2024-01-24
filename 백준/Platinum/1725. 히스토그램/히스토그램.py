N = int(input())
height = [int(input()) for _ in range(N)]

ans = 0
stack = []
for i in range(N):
    while stack and height[stack[-1]] > height[i]:
        h = height[stack.pop()]
        w = i - stack[-1] - 1 if stack else i
        ans = max(ans, h*w)
    stack.append(i)

while stack:
    h = height[stack.pop()]
    w = N - stack[-1] - 1 if stack else N
    ans = max(ans, h*w)

print(ans)