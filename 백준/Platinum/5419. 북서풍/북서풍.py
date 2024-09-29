for _ in range(int(input())):
    n = int(input())
    # x가 작은 순, y가 큰 순으로 정렬 
    arr = sorted([[*map(int, input().split()), i] for i in range(n)], key=lambda x: (x[0], -x[1]))
    # 세그먼트 트리에 사용될 y 좌표
    ys = sorted(set(v[1] for v in arr))
    # 특정 y 좌표가 세그먼트 트리에서 몇번째 노드인지 매핑 
    m = len(ys)
    ysi = {ys[i]: i for i in range(m)} 
    # 세그먼트 트리 생성
    size = 1
    while size < m:
        size <<= 1
    tree = [0] * (2 * size)
    # 스위핑
    ans = 0
    for x, y, i in arr:
        # 구간 쿼리
        l = size + ysi[y]
        r = 2 * size -1
        while l <= r:
            if l & 1:
                ans += tree[l]
                l += 1
            if not r & 1:
                ans += tree[r]
                r -= 1
            l >>= 1; r >>= 1
        # 구간 업데이트
        l = size + ysi[y]
        while l:
            tree[l] += 1
            l >>= 1
    # 출력
    print(ans)