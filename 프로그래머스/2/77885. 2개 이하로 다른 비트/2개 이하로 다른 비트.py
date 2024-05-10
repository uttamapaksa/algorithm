def solution(numbers):
    ans = []
    for num in numbers:
        N = len(bin(num)) - 2
        for i in range(N-1):
            if num & (1 << i) == 0:
                num |= (1 << i)
                if i:
                    num -= 1 << (i-1)
                break
        else:
            num += 1 << N
            num -= 1 << (N-1)
        ans.append(num)
    
    return ans