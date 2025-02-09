N, M = map(int, input().split())
enterList = list(map(int, input().split()))
value = 0
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            s = enterList[i] + enterList[j] + enterList[k]
            if s <= M:
                value = max(value, s)


print(value)