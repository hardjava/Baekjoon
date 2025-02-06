T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    no = N // H + 1
    if N % H == 0:
        floor = H
        no -= 1
    print("{0}{1:02d}".format(floor, no))