from heapq import heappop, heappush

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

heap = []
for node in range(1, N+1):
    if indegree[node]: continue
    finish[node] = task[node]
    heappush(heap, (finish[node], node))  # time, node

while heap:
    time, curr = heappop(heap)
    for next in child[curr]:
        indegree[next] -= 1
        if not indegree[next]:
            finish[next] = time + task[next]
            heappush(heap, (finish[next], next))

print(time)