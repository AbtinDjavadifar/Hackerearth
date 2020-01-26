N = int(input())
A =list(map(lambda x: int(x), input().split(' ')))
max = 0

# N = 10
# A = [2, 1, 3, 9, 2, 4, -10, -9, 1, 3]

for i in range(N):
    sum = 0
    B = A[i:].copy()
    j = 1
    while len(B) >= j:
        for k in range(j):
            sum += B.pop(0)
        j += 1
    if sum > max:
        max = sum

print(max)
