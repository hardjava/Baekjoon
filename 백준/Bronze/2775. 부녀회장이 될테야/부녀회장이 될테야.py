arr = [[i for i in range(15)] for _ in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = arr[i][j - 1] + arr[i - 1][j]

N = int(input())

for i in range(N):
    k = int(input())
    n = int(input())
    print(arr[k][n])