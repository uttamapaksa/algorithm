def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    l, r = len(left), len(right)
    i = j = 0
    sorted_arr = []

    while i < l and j < r:
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            cnt += l - i
    while i < l:
        sorted_arr.append(left[i])
        i += 1
    while j < r:
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr


N = int(input())
arr = [*map(int, input().split())]
cnt = 0
merge_sort(arr)
print(cnt)