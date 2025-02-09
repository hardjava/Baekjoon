N, M = map(int, input().split())

first = ['WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW']

arr = []
for i in range(N):
    arr.append(input())

def returnValue(startPoint):
    num1 = 0
    num2 = 0
    col = 0
    row = 0

    for i in range(startPoint[0], startPoint[0] + 8):
        for j in range(startPoint[1], startPoint[1] + 8):
            if arr[i][j] == first[row][col]:
                num2 += 1
            else:
                num1 += 1
            col += 1
        row += 1
        col = 0

    return min(num1, num2)

printValue = N * M

for i in range(0, N - 7):
    for j in range(0, M - 7):
        num = returnValue((i, j))
        printValue = min(printValue, num)

print(printValue)