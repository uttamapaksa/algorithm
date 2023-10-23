dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def complex(r, c):
    global apt
    if r < 0 or r == N or c < 0 or c == N or not(graph[r][c]):
        return
    graph[r][c] = 0
    apt += 1
    for k in range(4):
        complex(r + dr[k], c + dc[k])
    return apt

N = int(input())
graph = [[*map(int, input())] for _ in range(N)]

cnt = 0
aptcnt = []
for i in range(N):
    for j in range(N):
        apt = 0
        if graph[i][j]:
            aptcnt.append(complex(i, j))
            cnt += 1

print(cnt)
aptcnt.sort()
for i in aptcnt:
    print(i)