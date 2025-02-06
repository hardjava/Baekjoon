N = int(input())
l = []
for i in range(N):
    enter = int(input())
    if enter == 0:
        l.pop()
    else:
        l.append(enter)

print(sum(l))