def rotate(res, arr, x1, y1, x2, y2):
    idxs = []; vals = []
    # top
    for c in range(y1, y2): idxs.append((x1, c)); vals.append(arr[x1][c])
    # left
    for r in range(x1, x2): idxs.append((r, y2)); vals.append(arr[r][y2])
    # bot
    for c in range(y2, y1, -1): idxs.append((x2, c)); vals.append(arr[x2][c])
    # right
    for r in range(x2, x1, -1): idxs.append((r, y1)); vals.append(arr[r][y1])            
    # rotate 1 space
    idxs.append(idxs.pop(0))
    # allocate
    for i in range(len(idxs)):
        r, c = idxs[i]
        arr[r][c] = vals[i]
    # add min value
    res.append(min(vals))     


def solution(r, c, qs):
    arr = [[i*c+j for j in range(1, c+1)] for i in range(r)]
    
    res = []
    for x1, y1, x2, y2 in qs:
        rotate(res, arr, x1-1, y1-1, x2-1, y2-1)
    
    return res