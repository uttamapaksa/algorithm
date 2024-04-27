from heapq import heappop, heappush

L = []  # max heap
R = []  # min heap
heappush(R, 10001)

even = True
answer = []
for _ in range(int(input())):
    n = int(input())

    if even:
        if n <= R[0]:
            heappush(L, -n)
        else:
            heappush(L, -heappop(R))
            heappush(R, n)
    else:
        if n >= -L[0]:
            heappush(R, n)
        else:
            heappush(R, -heappop(L))
            heappush(L, -n)

    even = not even
    answer.append(str(-L[0]))

print("\n".join(answer))