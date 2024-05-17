def solution(n):
    pre = {'12':'13', '13':'12', '21':'31', '23':'32', '31':'21', '32':'23'}
    post = {'12':'21', '13':'23', '21':'12', '23':'13', '31':'32', '32':'31'}
    
    dp = []
    for _ in range(n):
        dp = [pre[v] for v in dp] + ['13'] + [post[v] for v in dp]
        
    return [list(map(int, v)) for v in dp]