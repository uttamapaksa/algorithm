def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    
    x1, y1 = sticker[0], 0
    x2, y2 = sticker[1], 0

    for i in range(1, n-1):
        x1, y1 = y1 + sticker[i], max(x1, y1)
    for i in range(2, n):
        x2, y2 = y2 + sticker[i], max(x2, y2)
        
    return max(x1, y1, x2, y2)