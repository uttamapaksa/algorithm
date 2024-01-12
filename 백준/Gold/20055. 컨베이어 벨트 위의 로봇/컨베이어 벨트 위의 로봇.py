from collections import deque
N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * N)
zero = 0
ans = 0


while zero < K:
    # turn
    robot.pop()
    robot.appendleft(0)
    belt.appendleft(belt.pop())

    # move robot
    robot[N-1] = 0
    for i in range(N-2, 0, -1):
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if not belt[i+1]:
                zero += 1

    # put new robot
    if belt[0]:
        robot[0] = 1
        belt[0] -= 1
        if not belt[0]:
            zero += 1

    # next step
    ans += 1


print(ans)