N = int(input())
l = list(map(int, input().split()))
T, P = map(int, input().split())
total = 0
for i in l:
    total = total + (i // T + 1)
    if i % T == 0:
        total -= 1

print(total)
print(N // P, N % P)