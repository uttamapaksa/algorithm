from collections import deque

def solution(n, k):
    
    def isPrime(k):
        if k in prime:
            return 1
        # k 자체가 소수일 경우 아래 반복문에 의해 False가 return됨
        # 아래의 반복문은 큰 수를 다루기 위해 logN 크기로 줄인 것이므로
        # 작은 소수는 그 이전에 판별해야 함
        for p in prime: 
            if not k % p:
                return 0
        return 1
    
    num = deque()
    while n:
        num.appendleft(str(n%k))
        n //= k
    
    cnt = {}
    for v in "".join(num).split("0"):
        if v and v != "1":
            # 뒤에 로직상 1은 prime에 추가할 수 없기 때문에 key=1은 소수 판정으로 제거를 못함
            # 그러니 1을 추가 안하도록 전처리 해야함
            v = int(v)
            # append() 했다면 여기서 v = int(v[::-1]) 뒤집어야 한다.
            # 아예 appendleft()로 저장했어야 안전하다.
            # 혹은 num[::-1]
            cnt[v] = cnt.get(v, 0) + 1
    
    if not len(cnt):
        return 0
    M = max(cnt)
    # 그런데 1이 제외되도록 전처리를 하면 key가 1일 뿐일 경우
    # 여기서 cnt가 빈 딕셔너리가 돼서 ValueError가 날 수 있음
    prime = set(range(2, int(M**0.5) + 1))
    for i in range(2, int(M**0.25) + 1):
        if i in prime:
            for j in range(i*i, int(M**0.5)+1, i):
                prime.discard(j)

    answer = 0
    for k, v in cnt.items():
        if isPrime(k):
            answer += v
    
    return answer