from collections import deque

def solution(stones, k):
    q = deque()
    mxa = []
    
    for idx, val in enumerate(stones):

        while q and q[-1][0] < val:
            q.pop()
        q.append((val, idx))

        while idx - q[0][1] >= k:
            q.popleft()
        mxa.append(q[0][0])

    return min(mxa[k-1:])