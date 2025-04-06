from collections import deque

def solution(priorities, location):
    d = deque()
    answer = 1
    
    for i in range(len(priorities)):
        d.append((priorities[i], i))
    while True:
        maxValue = max(d)[0]
        while d[0][0] != maxValue:
            temp = d[0]
            d.popleft()
            d.append(temp)
        if d[0][1] == location:
            return answer
        else:
            d.popleft()
            answer += 1
    
    return answer