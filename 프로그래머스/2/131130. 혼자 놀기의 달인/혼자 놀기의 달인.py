def solution(cards):
    n = len(cards)
    cards = [0] + cards
    visit = [0] * (n+1)
    
    ans = [0]
    for i in range(1, n+1):
        if visit[i]: continue
        u = i
        cnt = 0
        while not visit[u]:
            visit[u] = 1
            cnt += 1
            u = cards[u]
        ans.append(cnt)
    ans.sort(reverse=True)
    
    return ans[0] * ans[1]
    
    