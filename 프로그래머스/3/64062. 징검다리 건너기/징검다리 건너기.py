def solution(stones, k):
    n = len(stones)
    stones = [(v, i) for i, v in enumerate(stones)]
    stones.sort(reverse=True)
    V = [0] * (n)
    SE = [[i, i] for i in range(n)]  # [start, end][]
    cnt = 0
    
    while stones:
        mn, idx = stones.pop()
        curr = [idx]
        V[idx] = 1
        while stones and stones[-1][0] == mn:
            idx = stones.pop()[1]
            curr.append(idx)
            V[idx] = 1
            
        for idx in curr:
            if idx > 0 and V[idx-1]:
                SE[idx][0] = SE[idx-1][0]
            if idx < n-1 and V[idx+1]:
                SE[idx][1] = SE[idx+1][1]
            SE[SE[idx][0]][1] = SE[idx][1]
            SE[SE[idx][1]][0] = SE[idx][0]
            if SE[idx][1] - SE[idx][0] + 1 >= k:
                return mn
        
        cnt = mn
    return cnt