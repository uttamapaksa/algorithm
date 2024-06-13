N = int(input())
task = [0] * (N+1)
child = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
finish = [0] * (N+1)

for node in range(1, N+1):
    tmp = [*map(int, input().split())]
    task[node] = tmp[0]  # task_time
    indegree[node] = tmp[1]  # parent_cnt
    for par in tmp[2:]:
        child[par].append(node)

queue = []
for node in range(1, N+1):
    if indegree[node]: continue
    finish[node] = task[node]
    queue.append((finish[node], node))  # time, node

while queue:
    time, curr = queue.pop()
    for next in child[curr]:
        finish[next] = max(finish[next], time + task[next])
        indegree[next] -= 1
        if not indegree[next]:
            queue.append((finish[next], next))  # time, node

print(max(finish[1:]))