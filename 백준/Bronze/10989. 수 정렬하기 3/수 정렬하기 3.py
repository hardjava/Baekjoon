N = int(input())
idxList = [0] * 10001

for i in range(N):
    enter = int(input())
    idxList[enter] += 1

for i in range(len(idxList)):
    if idxList[i] != 0:
        for j in range(idxList[i]):
            print(i)