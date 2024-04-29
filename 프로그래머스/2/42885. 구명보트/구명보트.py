from collections import deque

def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    
    while people:
        first = people.pop()
        if people and first + people[0] <= limit:
            people.popleft()
        answer += 1
    
    return answer