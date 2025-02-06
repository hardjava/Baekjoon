n = int(input())
s = []
for i in range(n):
    enter = list(input().split())
    if enter[0] == 'push':
        s.append(enter[1])
    elif enter[0] == 'size':
        print(len(s))
    elif enter[0] == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif enter[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif enter[0] == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])