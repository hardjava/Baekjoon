q = list()

N = int(input())

for i in range(N):
    l = list(map(str, input().split()))
    if l[0] == 'push':
        q.append(int(l[1]))
    elif l[0] == 'front':
        if sum(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif l[0] == 'pop':
        if sum(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.pop(0)
    elif l[0] == 'size':
        print(len(q))
    elif l[0] == 'empty':
        print(int(len(q) == 0))
    elif l[0] == 'back':
        if sum(q) == 0:
            print(-1)
        else:
            print(q[-1])