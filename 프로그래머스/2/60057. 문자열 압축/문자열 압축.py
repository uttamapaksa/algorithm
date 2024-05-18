def solution(s):
    n = len(s)
    ans = n
    
    for i in range(1, n//2 + 1):
        stack = []
        for j in range(0, n, i):
            ss = s[j:j+i]
            if not stack or stack[-1][0] != ss:
                stack.append([ss, 1])
            else:
                stack[-1][1] += 1
                
        curr = 0
        for ss, cnt in stack:
            curr += len(ss)
            if cnt > 1:
                curr += len(str(cnt))
        ans = min(ans, curr)
            
    return ans