N = int(input())
l = []
for i in range(N):
    x, y = map(int, input().split())
    l.append((x, y))

l = sorted(l, key= lambda x: (x[0], x[1]))

for i in l:
    print(i[0], i[1])