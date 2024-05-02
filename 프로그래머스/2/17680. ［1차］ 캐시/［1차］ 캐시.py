from collections import deque

def solution(size, cities):
    if not size:
        return 5 * len(cities)
    
    answer = 0
    Q = deque()
    
    for city in cities:
        city = city.lower() 
        if city in Q:
            Q.remove(city)
            Q.append(city)
            answer += 1
        else:
            if len(Q) == size:
                Q.popleft()
            Q.append(city)  
            answer += 5
        
    return answer