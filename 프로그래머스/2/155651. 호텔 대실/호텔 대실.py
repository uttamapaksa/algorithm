from heapq import heappush, heappop

def solution(book_time):
    se = []
    for s, e in book_time:
        sh, sm = s.split(':')
        eh, em = e.split(':')
        se.append((int(sh)*60 + int(sm), int(eh)*60 + int(em)+10))
    se.sort()
    
    heap = []
    for s, e in se:
        if heap and heap[0][0] <= s:
            heappop(heap)
        heappush(heap, (e, s))

    return len(heap)