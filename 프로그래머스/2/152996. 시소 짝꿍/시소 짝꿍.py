def solution(weights):
    cnt = {}
    for weight in weights:
        cnt[weight] = cnt.get(weight, 0) + 1
    n = len(cnt)
    cnt = sorted(cnt.items())
    
    ans = 0
    for i in range(n):  # cnt[n]끼리도 계산해야 하니까 n-1이 아닌 n까지 해야 한다
        w1, c1 = cnt[i]
        ans += (c1*(c1-1)) // 2
        for j in range(i+1, n):
            w2, c2 = cnt[j]
            if w1*4 > w2*3: continue
            if w1*2 < w2: break
            if w1*2 == w2 or w1*3 == w2*2 or w1*4 == w2*3:
                ans += c1*c2
                
    return ans