N = int(input())

num = 1
value = 666

while num < N:
    value += 1
    if str(value).find('666') != -1:
        num += 1

print(value)