N = int(input())

def printValue(N: int):
    for i in range(1, N):
        s = str(i)
        total = i
        for j in s:
            total += int(j)
        if total == N:
            print(i)
            return
    print(0)

printValue(N)