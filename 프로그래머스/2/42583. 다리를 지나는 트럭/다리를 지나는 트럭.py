from collections import deque

def solution(bridge_length, limit, trucks):
    trucks = deque(trucks)
    bridge = deque([0] * bridge_length)
    weight = 0
    time = 0
    
    while weight or trucks:
        time += 1
        weight -= bridge.popleft()
        if trucks and trucks[0] + weight <= limit:
            bridge.append(trucks[0])
            weight += trucks.popleft()
        else:
            bridge.append(0)
        
    return time