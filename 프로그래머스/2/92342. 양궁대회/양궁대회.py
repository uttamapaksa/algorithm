def solution(n, info):
    max_score = 0
    ans = [-1]
    
    def comb(i, r, score, p):
        if i == 10:
            if score > 0:
                nonlocal max_score, ans
                p += [r]
                if max_score == score:
                    # 가장 낮은 점수가 가장 높음
                    ans = max(ans[::-1], p[::-1])[::-1]
                elif max_score < score:
                    max_score = score
                    ans = p
            return
        # 라이언 승
        if info[i] < r:
            comb(i+1, r-(info[i]+1), score+10-i, [*p]+[info[i]+1])
        # 어피치 승
        if info[i]:
            comb(i+1 , r, score-(10-i), [*p]+[0])
        # 둘다 0, 무승부
        else:
            comb(i+1 , r, score, [*p]+[0])
    comb(0, n, 0, [])
    
    return ans