def solution(n, wires):
    
    def count(u):
        if child[u]:
            return 0
        child[u] = 1
        for v in tree[u]:
            child[u] += count(v)
        return child[u]
    
    
    child = [0] * (n+1)
    tree = [[] for _ in range(n+1)]
    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)
    count(1)
        
    answer = min(abs(n - 2*c) for c in child)
    return answer