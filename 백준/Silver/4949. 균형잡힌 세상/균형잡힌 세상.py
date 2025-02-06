def printValue(enter=str):
    l = []

    for i in enter:
        if i == '(' or i == '[':
            l.append(i)
        elif i == ')' or i == ']':
            if len(l) == 0:
                print('no')
                return
            elif i == ')' and l[-1] != '(':
                print('no')
                return
            elif i == ']' and l[-1] != '[':
                print('no')
                return
            l.pop()                
    
    if len(l) == 0:
        print('yes')
    else:
        print('no')


while True:
    enter=input()
    if enter == '.':
        break
    
    printValue(enter)
