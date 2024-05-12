def solution(n):
    map = ['1','2','4']
    ans = []
    
    while n:
        n, m = divmod(n-1, 3)
        ans.append(map[m])
        
    return ''.join(ans[::-1])