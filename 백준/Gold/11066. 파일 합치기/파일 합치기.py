import sys; input=sys.stdin.readline

for _ in range(int(input())):
    전체개수, 전체배열 = int(input()), list(map(int, input().split()))

    for 현재인덱스 in range(1, 전체개수):
        전체배열[현재인덱스] += 전체배열[현재인덱스 - 1]

    누적비용테이블 = [[0] * 전체개수 for _ in range(전체개수)]

    for 길이 in range(2, 전체개수 + 1):
        for 시작인덱스 in range(전체개수 - 길이 + 1):
            끝인덱스 = 시작인덱스 + 길이 - 1
            누적비용테이블[시작인덱스][끝인덱스] = float('inf')

            for 중간인덱스 in range(시작인덱스, 끝인덱스):
                현재비용 = 누적비용테이블[시작인덱스][중간인덱스] + 누적비용테이블[중간인덱스 + 1][끝인덱스] + 전체배열[끝인덱스] - (전체배열[시작인덱스 - 1] if 시작인덱스 > 0 else 0)
                누적비용테이블[시작인덱스][끝인덱스] = min(누적비용테이블[시작인덱스][끝인덱스], 현재비용)

    print(누적비용테이블[0][전체개수 - 1])