for _ in range(int(input())):
    n = int(input())
    # x가 큰 순, y가 작은 순으로 정렬
    arr = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], x[1]))
    # 좌표 압축. 펜윅 트리에 사용될 y 좌표
    ys = sorted(set(v[1] for v in arr)) 
    # 특정 y 좌표가 펜윅 트리에서 몇번째 노드인지 매핑. sum(0) - sum(-1)을 방지하기 위해 i + 1
    m = len(ys)
    ysi = {ys[i]: i + 1 for i in range(m)} 
    # 펜윅 트리 생성
    tree = [0] * (m + 1)
    # 스위핑
    ans = 0
    for x, y in arr:
        # 구간 쿼리
        # 이 문제는 y가 더 높은 점들이 이전 점들인데, 펜윅 트리는 무조건 트리의 0번째 노드부터 더하기 때문에 이후 점들을 먼저 계산
        # 그래서 거꾸로 이후 점에서 이전 점으로 누적합으로 구하기 위해서 arr를 y가 작은(이후 점) 순으로 정렬해야 함
        idx = ysi[y]
        while idx > 0:
            ans += tree[idx]
            idx -= idx & -idx
        idx = ysi[y]
        cnt = 1
        # 구간 업데이트
        while idx <= m:
            cnt += 1
            tree[idx] += 1
            idx += idx & -idx
    # 출력
    print(ans)
