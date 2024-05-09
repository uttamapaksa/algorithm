def solution(land):
    for i in range(1, len(land)):
        for c1, p1, p2, p3 in ((0, 1, 2, 3), (1, 0, 2, 3), (2, 0, 1, 3), (3, 0, 1, 2)):
            land[i][c1] += max(land[i-1][p1], land[i-1][p2], land[i-1][p3])
    
    return max(land[-1])