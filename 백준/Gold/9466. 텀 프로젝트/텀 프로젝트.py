for _ in range(int(input())):
    N = int(input())
    arr = [0] + [*map(int, input().split())]
    visit = [0] * (N + 1)
    team = []

    for start_student in range(1, N + 1):
        if visit[start_student]: continue  # 방문한 학생이면

        now_cycle = []
        now_student = start_student
        while 1:
            visit[now_student] = 1
            now_cycle.append(now_student)
            next_student = arr[now_student]

            if visit[next_student]:  # 방문한 학생일 때
                if next_student in now_cycle:
                    # 그 학생이 현재의 싸이클에 있으면(이번 싸이클에 처음 방문한 학생이면)
                    team += now_cycle[now_cycle.index(next_student):]
                    # 그 학생이 처음 나온 인덱스부터 끝(그 학생이 다시 나온 인덱스)까지의 싸이클을 팀에 넣음
                break
            now_student = next_student

    print(N - len(team))