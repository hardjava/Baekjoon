def round(num):
    strNumArr = str(num).split('.')
    if int(strNumArr[1][0]) >= 5:
        if num >= 0:
            return int(strNumArr[0]) + 1
        else:
            return int(strNumArr[0]) - 1
    else:
        return int(strNumArr[0])
        
N = int(input())
l = []
for i in range(N):
    l.append(int(input()))

l.sort()

cutNum = N * 0.15
cutNum = round(cutNum)
s = 0
for i in range(cutNum, N - cutNum):
    s += l[i]

if (N-cutNum * 2) == 0:
    print(0)
else:
    avg = round(s / (N - cutNum * 2))
    print(avg)