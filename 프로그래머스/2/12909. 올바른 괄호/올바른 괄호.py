def solution(s):
    answer = True
    my_stack = []
    
    for i in s:
        if i == '(':
            my_stack.append(i)
        elif i == ')':
            if len(my_stack) == 0:
                return False
            elif my_stack[-1] != '(':
                return False
            elif my_stack[-1] == '(':
                my_stack.pop()
    
    if len(my_stack) == 0:
        return True
    
    return False