N, M = map(int, input().split())
a = N
b = M
if N < M:
    temp = M
    M = N
    N = temp

while M > 0:
    remain = N % M
    N = M
    M = remain

print(N)
print((a // N) * (b // N) * N)