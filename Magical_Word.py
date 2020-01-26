primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

T = int(input())
# T = 1

for _ in range(T):
    N = int(input())
    # N = 6
    S = input()
    # S = 'AFREEN'
    out = []
    for n, l in enumerate(S):
        diff = [abs(ord(l) - i) for i in primes]
        w = diff.index(min(diff))
        out.append(chr(primes[w]))
    print(''.join(out))