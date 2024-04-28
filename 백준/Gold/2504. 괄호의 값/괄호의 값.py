def isValid():
    stack = []
    for i in arr:
        if i == ")":
            if not stack or stack.pop() != "(":
                return 0
        elif i == "]":
            if not stack or stack.pop() != "[":
                return 0
        else:
            stack.append(i)
    if stack:
        return 0
    return 1


def sol():
    if not isValid():
        return 0

    stack = []
    for i in arr:
        if i == "(" or i == "[":
            stack.append(i)
            stack.append(0)
        elif i == ")":
            tmp = 0
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()
            stack.append(2 * tmp or 2)
        else:
            tmp = 0
            while stack[-1] != "[":
                tmp += stack.pop()
            stack.pop()
            stack.append(3 * tmp or 3)

    return sum(stack)


arr = [*input()]
print(sol())