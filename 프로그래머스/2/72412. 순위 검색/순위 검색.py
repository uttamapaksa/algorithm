from bisect import bisect_left

def solution(infos, querys):
    trie = {}
    answer = []
    
    n = len(infos)
    for info in infos:
        a, b, c, d, e = info.split()
        e = int(e)
        node = trie
        if a not in node:
            node[a] = {}
        node = node[a]
        if b not in node:
            node[b] = {}
        node = node[b]
        if c not in node:   
            node[c] = {}
        node = node[c]
        if d not in node:
            node[d] = []
        node = node[d]
        node.append(e)
        node.sort()
    
    for query in querys:
        a, b, c, de = query.split(" and ")
        d, e = de.split()
        e = int(e)
        
        nodes = [trie]
        curr = []
        for node in nodes:
            for key in node:
                if a == "-" or a == key:
                    curr.append(node[key])
        nodes = curr
        curr = []
        for node in nodes:
            for key in node:
                if b == "-" or b == key:
                    curr.append(node[key])
        nodes = curr
        curr = []
        for node in nodes:
            for key in node:
                if c == "-" or c == key:
                    curr.append(node[key])
        nodes = curr
        curr = {}
        cnt = 0
        for node in nodes:
            for key in node:
                val = node[key]
                if d == "-" or d == key:
                    tmp = bisect_left(val, e)
                    cnt += len(val) - tmp
        
        answer.append(cnt)
        
    return answer