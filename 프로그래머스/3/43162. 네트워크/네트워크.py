def isAllVisited(visited):
    for i in range(1, len(visited)):
        if visited[i] == False:
            return False
    return True

def solution(n, computers):
    visited = [False] * (n + 1)
    s = []
    s.append(1)
    answer = 0
    while isAllVisited(visited) == False:
        if len(s) > 0:
            visit = s[-1]
            s.pop()
            visited[visit] = True
            for i in range(n):
                if computers[visit - 1][i] == 1 and visited[i + 1] == False:
                    s.append(i + 1)        
        else:
            answer += 1
            for i in range(1, len(visited)):
                if visited[i] == False:
                    s.append(i)
                    break
                    
    answer+= 1
    return answer