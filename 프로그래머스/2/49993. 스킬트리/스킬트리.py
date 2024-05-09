def solution(skill, skill_trees):
    skill_set= set(skill)
    
    ans = 0
    for skill_tree in skill_trees:
        front = 0
        for curr in skill_tree:
            if curr not in skill_set: continue
            if curr != skill[front]: break
            front += 1
        else:
            ans += 1
            
    return ans