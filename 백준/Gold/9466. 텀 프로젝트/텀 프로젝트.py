import sys; input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [0] + [*map(int, input().split())]
    visit = [0] * (N + 1)
    solo_students = N  # 소속된 팀이 없는 학생 수

    for now_student in range(1, N + 1):
        if visit[now_student]: continue  # 방문한 학생이면

        now_cycle = []
        len_cycle = 1
        while 1:
            visit[now_student] = 1
            now_cycle.append(now_student)
            next_student = arr[now_student]

            if visit[next_student]:  # 방문한 학생일 때
                if next_student in now_cycle:
                    # 그 학생이 현재의 싸이클에 있으면(이미 한번 나와서 싸이클을 만들 수 있는 학생이면)
                    solo_students -= (len_cycle - now_cycle.index(next_student))
                    # 그 학생이 처음 나온 인덱스부터 끝(그 학생이 다시 나오기 직전 인덱스)까지의 싸이클 길이를 뺌
                break
            now_student = next_student
            len_cycle += 1

    print(solo_students)