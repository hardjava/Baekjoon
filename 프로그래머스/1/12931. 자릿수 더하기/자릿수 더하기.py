def solution(n):
    l = []
    
    while n > 0:
        remain = n % 10
        n = n // 10
        l.append(remain)
    
    answer = sum(l)
    
    return answer