from collections import Counter

T = int(input())
# T = 1

for _ in range(T):
    S = list(input())
    # S = 'abccba'
    out = 0
    for start in range(len(S)):
        for step in range(len(S) - start):
            sub = S[start : start + step + 1]
            if len(sub) % 2 == 0:
                # words = Counter(sub).keys()
                count = Counter(sub).values()
                if all(i % 2 == 0 for i in count):
                    out += 1
    print(out)