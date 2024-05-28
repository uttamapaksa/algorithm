def solution(name):
    n = len(name)
    ans = 0

    updown = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]
    ans += sum(updown)

    leftright = n - 1
    for i in range(n):
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
        right_back_left = i + i + n - next 
        left_back_right = n - next + n - next + i
        leftright = min(leftright, right_back_left, left_back_right)
    ans += leftright

    return ans

