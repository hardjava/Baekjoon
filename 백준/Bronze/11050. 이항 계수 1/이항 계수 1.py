N, K = map(int, input().split())

arr = [[1] * 11 for _ in range(11)]

for i in range(2, 11):
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]

print(arr[N][K])