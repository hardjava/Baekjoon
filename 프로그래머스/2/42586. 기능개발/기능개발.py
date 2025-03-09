def solution(progresses: list, speeds: list):
    day = []
    result = []
    for i in range(len(progresses)):
        firstProgress = progresses[i]
        firstSpeed = speeds[i]
        term = (100 - firstProgress) // firstSpeed
        if (100 - firstSpeed) % firstSpeed != 0:
            term += 1
        day.append(term)

    while sum(day) > 0:
        count = 1
        first = day[0]
        day.pop(0)
        while sum(day) > 0 and day[0] <= first:
            day.pop(0)
            count += 1
        result.append(count)
    return result