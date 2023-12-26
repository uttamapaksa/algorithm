arr = [[*map(int, input().split())] for _ in range(10)]
one = [(i, j) for i in range(10) for j in range(10) if arr[i][j]]
paper = [5] * 6 # remaining paper count
visit = set()
ans = 30

# return whether it can be covered or not
def promising(p, r, c):
    if r+p > 10 or c+p > 10: 
        return 0
    for i in range(r, r+p):
        for j in range(c, c+p):
            if not arr[i][j] or (i, j) in visit: 
                return 0
    if paper[p]:
        return 1

def sol(k):
    global visit, ans
    if k >= ans: # pruning
        return
    for r, c in one: # remaining one
        if (r, c) not in visit:
            break
    else: # done, update ans
        ans = min(ans, k)
        return
    
    for p in range(5, 0, -1): # greedy brute force search
        if promising(p, r, c): # paper size, row, col
            curr_visit = {(i, j) for i in range(r, r+p) for j in range(c, c+p)}
            visit |= curr_visit
            paper[p] -= 1
            sol(k+1)
            visit -= curr_visit # backtracking
            paper[p] += 1
sol(0)

print(ans if ans != 30 else -1)