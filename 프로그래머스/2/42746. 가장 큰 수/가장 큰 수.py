def solution(numbers):
    numbers = [*map(str, numbers)]
    numbers.sort(key=lambda x: x*3, reverse=True)
    if not int(numbers[0]):
        return "0"
    else:
        return "".join(numbers)