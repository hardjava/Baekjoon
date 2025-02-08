l = []
idx = 0
for i in range(3):
    enter = str(input())
    if enter.isnumeric():
        idx = i
    l.append(enter)

number = int(l[idx]) + (3 - idx)

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0 and number % 5 != 0:
    print('Fizz')
elif number % 3 != 0 and number % 5 == 0:
    print('Buzz')
else:
    print(number)