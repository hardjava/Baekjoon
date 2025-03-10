from collections import deque

def solution(numbers: list, target):
    d = deque()
    d.append(numbers[0])
    d.append(-numbers[0])

    for i in range(1, len(numbers)):
        length = len(d)
        for _ in range(length):
            front = d[0]
            d.popleft()
            d.append(front + numbers[i])
            d.append(front - numbers[i])

    result = d.count(target)
    return result


