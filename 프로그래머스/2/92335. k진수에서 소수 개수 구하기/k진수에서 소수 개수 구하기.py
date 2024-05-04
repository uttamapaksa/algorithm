def solution(n, k):
    
    def isPrime(k):
        if k == 1:
            return 0
        if k == 2:
            return 1
        for i in range(2, int(k**0.5)+1):
            if not k % i:
                return 0
        return 1
    
    num = []
    while n:
        num.append(str(n%k))
        n //= k
    num = num[::-1]
    
    cnt = {}
    for v in "".join(num).split("0"):
        if v :
            v = int(v)
            cnt[v] = cnt.get(v, 0) + 1
    num = 0
    
    answer = 0
    for k, v in cnt.items():
        if isPrime(k):
            answer += v
    
    return answer