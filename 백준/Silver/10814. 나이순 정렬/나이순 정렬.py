N = int(input())
enter = []

for i in range(N):
    age, name = map(str, input().split())
    enter.append((i, int(age), name))

enter = sorted(enter, key= lambda x: (x[1], x[0]))

for i in enter:
    print(i[1], i[2])