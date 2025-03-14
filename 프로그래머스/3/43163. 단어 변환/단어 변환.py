def getDifferentCount(a: str, b: str):
    differentCount = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            differentCount += 1

    return differentCount

def solution(begin, target, words):
    visited = [False] * len(words)
    visitCount = []
    def visit(currentStr: str, count):
        if currentStr == target:
            visitCount.append(count)
            return

        for i in range(len(words)):
            if visited[i] == False and getDifferentCount(currentStr, words[i]) == 1:
                visited[i] = True
                visit(words[i], count + 1)
                visited[i] = False

    visit(begin, 0)
    if len(visitCount) == 0:
        return 0
    return min(visitCount)