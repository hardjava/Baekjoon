n = int(input())
enterList = []
for i in range(n):
    enterList.append(int(input()))

enterList.sort()

for i in enterList:
    print(i)