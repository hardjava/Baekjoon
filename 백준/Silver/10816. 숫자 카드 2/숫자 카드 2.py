N = int(input())

d = {}

for i in list(map(int, input().split())):
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] += 1

M = int(input())

for i in list(map(int, input().split())):
    if d.get(i) == None:
        print(0, end=' ')
    else:
        print(d[i], end=' ')