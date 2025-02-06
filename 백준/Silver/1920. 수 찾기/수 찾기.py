N = int(input())
l = list(map(int, input().split()))
dic = {}

for i in l:
    dic[i] = True

M = int(input())
enter = list(map(int, input().split()))

for i in enter:
    if dic.get(i) != None:
        print(1)
    else:
        print(0)