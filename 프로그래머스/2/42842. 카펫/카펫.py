def solution(brown, muls):
    sums = int((brown - 4) / 2)
    
    start = 1
    end = sums - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        x = max(sums - mid, mid)
        y = sums - x
        
        if muls == x * y:
            return [x+2, y+2]
        if muls > x * y:
            end = mid - 1
        else:
            start = mid + 1
        