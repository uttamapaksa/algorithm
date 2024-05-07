def solution(arr):
    N = len(arr)
    ans = list(range(N-1, -1, -1))
    
    stack = []
    for i in range(N):
        while stack and stack[-1][1] > arr[i]:
            ans[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append((i, arr[i]))
    
    return ans