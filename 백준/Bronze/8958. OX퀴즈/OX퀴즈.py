n = int(input())

for i in range(n):
    input_str = input()
    num = 0
    sum = 0
    for i in input_str:
        if i == 'O':
            num += 1
        else:
            num = 0
        sum += num
    print(sum)