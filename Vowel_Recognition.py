T = int(input())

for _ in range(T):
    out = 0
    S = list(input())
    for i, char in enumerate(S):
        if char in 'aeiouAEIOU':
            out += (len(S) - i) * (i + 1)
    print(out)