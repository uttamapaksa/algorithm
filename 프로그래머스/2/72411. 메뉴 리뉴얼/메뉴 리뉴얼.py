from itertools import combinations

def solution(orders, course):
    count = {}
    
    for order in orders:
        for num in course:
            for comb in combinations(order, num):
                menu = ''.join(sorted(comb))
                if menu in count:
                    count[menu] += 1
                else:
                    count[menu] = 1

    maxcnt = {i: 0 for i in range(2, 11)}
    course = {i: [] for i in range(2, 11)}
    for menu in count:
        if count[menu] < 2: continue
        l = len(menu)
        if maxcnt[l] == count[menu]:
            course[l].append(menu)
        elif maxcnt[l] < count[menu]:
            course[l] = [menu]
            maxcnt[l] = count[menu]
            
    answer = []
    for key in course.values():
        answer.extend(key)
    
    
    answer.sort()
    return answer