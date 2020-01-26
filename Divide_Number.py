from functools import reduce
from itertools import combinations_with_replacement

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

T = int(input())

for _ in range(T):
    N = int(input())
    out = -1
    candidates = combinations_with_replacement(list(factors(N)), 4)
    for candidate in candidates:
        multiply = reduce((lambda x, y: x * y), candidate)
        if sum(candidate) == N and multiply > out:
            out = multiply
    print(out)
