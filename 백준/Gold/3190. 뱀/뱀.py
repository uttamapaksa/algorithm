from collections import deque


def canGo(d):
    global r, c
    dr, dc = delta[d]
    r, c = r + dr, c + dc
    if 1<=r<N+1 and 1<=c<N+1 and (r,c) not in snakeSet:
        snake.append((r,c)) # snake goes
        snakeSet.add((r,c))
        if (r,c) in apple: # eat apple
            apple.remove((r,c))
        else: # not eat apple
            snakeSet.remove(snake.popleft())
        return 1
    return 0


def game():
    time, d = 0, 0
    for X, C in order:
        X = int(X) - time
        for _ in range(int(X)):
            if canGo(d):
                time += 1
            else:
                return time
        if C == 'L':
            d = (d+3) % 4
        else:
            d = (d+1) % 4
    while canGo(d):
        time += 1
    return time


N, K  = int(input()), int(input())
apple = {tuple(map(int, input().split())) for _ in range(K)}
L = int(input())
order = [input().split() for _ in range(L)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = deque([(1, 1)])
snakeSet = {(1, 1)}
r = c = 1

print(game() + 1)