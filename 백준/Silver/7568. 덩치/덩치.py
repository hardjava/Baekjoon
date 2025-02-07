N = int(input())

input_l = []
d = {}

for i in range(N):
    w, h = map(int, input().split())
    input_l.append((w, h))
    d[(w, h)] = 1

l = sorted(input_l, reverse=True)

for i in range(1, len(l)):
    cur = l[i]
    if d[cur] == 1:
        for j in range(0, i):
            prev = l[j]
            if cur[0] < prev[0] and cur[1] < prev[1]:
                d[cur] += 1

for i in input_l:
    print(d[i], end=' ')