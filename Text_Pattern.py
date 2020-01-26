# T = int(input())
T = 1

for _ in range(T):
    inp = 'thisismytext text'
    text, pattern = map(lambda x : list(x) , inp.split(' '))
    starts = [i for i, x in enumerate(text) if x == pattern[0]]
    deleted = 0
    for start in starts:
        index_text = start
        index_pattern = 1
        steps = 0
        while index_pattern <= len(pattern):
            try:
                next = min([i for i, x in enumerate(text[index_text + 1:]) if x == pattern[index_pattern]])
                steps += next - index_text
                index_text = next
                index_pattern += 1
            except ValueError:
                break
        if (index_pattern > len(pattern)) and (steps > deleted):
            deleted = steps
    if deleted > 0:
        print('Yes', deleted)
    else:
        print('No')

