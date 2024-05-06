def solution(word):
    to_int = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    dp = [1]
    for _ in range(4):
        dp.append(dp[-1] * 5 + 1)
    dp = dp[::-1]
    
    ans = 0
    for i in range(len(word)):
        ans += to_int[word[i]] * dp[i] + 1
    
    return ans
