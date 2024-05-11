from itertools import permutations

def solution(numbers):
    
    def prime(k):
        if k <= 1: return 0
        if k <= 3: return 1
        for i in range(2, int(k**0.5)+1):
            if not k % i:
                return 0
        return 1
    
    N = len(numbers)
    numbers = [*map(str, numbers)]
    numbers = {int("".join(comb)) for i in range(1, N+1) for comb in permutations(numbers, i)}
    
    ans = sum(prime(num) for num in numbers)
    return ans