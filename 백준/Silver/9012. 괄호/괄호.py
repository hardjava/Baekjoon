def printValue(enter=str):
    l = []
    for i in enter:
        if i == '(':
            l.append(i)
        elif i == ')':
            if len(l) == 0:
                print('NO')
                return
            elif l[-1] != '(':
                print('NO')
                return
            l.pop()
    
    if len(l) == 0:
        print('YES')
    else:
        print('NO')

N = int(input())

for i in range(N):
    enter = input()

    printValue(enter)