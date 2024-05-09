def solution(order):
    order = order[::-1]
    n = len(order)
    init = list(range(n, 0, -1))
    stack = []
    
    while order:
        if init and order[-1] == init[-1]:
            order.pop()
            init.pop()
            continue
        if stack and order[-1] == stack[-1]:
            order.pop()
            stack.pop()
            continue
        while init and order[-1] > init[-1]:
            stack.append(init.pop())
        if init and order[-1] < init[-1]:
            break
        if not init and order[-1] != stack[-1]:
            break
            
    return n - len(order)