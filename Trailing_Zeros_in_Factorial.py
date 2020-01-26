T = int(input())

for _ in range(T):
    M = int(input())
    i = 0
    up = 0
    while M >= up:
        i += 1
        up += 5**i - 1
    if M == up:
        ans = 5**i - 5
        print(ans, ans + 1, ans + 2, ans + 3 , ans + 4)
        break
    fives = up - (5**i - 1) + i
    diff = M - fives
    compensate = 0
    added_five = 0
    while compensate < diff:
        added_five += 1
        compensate += 1
        for n in range(1, i):
            if added_five % 5**n == 0:
                compensate += 1
    ans = 5**i + added_five * 5
    if compensate == diff:
        print(5)
        print(ans, ans + 1, ans + 2, ans + 3, ans + 4)
    else:
        print(0)