N, K = map(int, input().split())

l = [i for i in range(1, N + 1)]
num = 0
print('<', end='')

while len(l) > 1:
    first = l[0]
    l.pop(0)
    if num == K - 1:
        print(first, end=', ')
        num = 0
    else:
        l.append(first)
        num += 1

print("{0:0d}>".format(l[0]))