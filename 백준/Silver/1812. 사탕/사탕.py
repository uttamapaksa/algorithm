N = int(input())
arr = [int(input()) for _ in range(N)]
candy = (sum(arr[i] for i in range(0, N, 2)) - sum(arr[i] for i in range(1, N, 2))) // 2

print(candy)
for i in range(N-1):
    candy = arr[i] - candy
    print(candy)