K, N = map(int, input().split())
l = [0] * K 

l[0] = int(input())
maxValue = l[0]

for i in range(1, K):
    l[i] = int(input())
    maxValue = max(maxValue, l[i])

start = 1
end = maxValue
value = 0

while start <= end:
    middle = (start + end) // 2
    totalNum = 0
    for i in l:
        totalNum = totalNum + i // middle
    
    if totalNum >= N:
        value = max(middle, value)
        start = middle + 1
    else:
        end = middle - 1

print(value)