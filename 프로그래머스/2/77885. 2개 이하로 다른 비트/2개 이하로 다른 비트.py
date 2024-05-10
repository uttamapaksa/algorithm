def solution(numbers):
    ans = []
    
    for num in numbers:
        i = 0
        while True:
            if not num & (1 << i):
                num += 1 << i
                if i:
                    num -= 1 << (i-1)
                break
            i += 1
        ans.append(num)
    
    return ans