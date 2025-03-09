def solution(array, commands):
    answer = []
    
    for c in commands:    
        newArr = array[c[0] - 1: c[1]]
        newArr.sort()
        answer.append(newArr[c[2] - 1])
    
    return answer