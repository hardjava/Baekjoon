N = int(input())
enter = {}
for i in range(N):
    str = input()
    enter[str] = True

enterList = enter.keys()
enterList = sorted(enterList, key= lambda x: (len(x), x))

for i in enterList:
    print(i)