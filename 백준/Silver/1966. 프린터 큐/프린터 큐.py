a = int(input())

for i in range(a):
    l = []
    N, M = map(int, input().split())
    idx = 0
    for j in list(map(int, input().split())):
        l.append((j, idx))
        idx += 1

    num = 0
    while True:
        maxPrior = max(l)
        while l[0][0] != maxPrior[0]:
            temp = l[0]
            l.pop(0)
            l.append(temp)

        num += 1
        if l[0][1] == M:
            print(num)
            break
        else:
            l.pop(0)