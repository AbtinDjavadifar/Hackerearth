# S = 'All-convoYs-9-be:Alert1.'
# N = 4

S = input()
N = int(input())
out = list(S)

for i, l in enumerate(S):
    if l.isalnum():
        if ord(l)<58:
            out[i] = chr((ord(l)- 48 + N) % 10 + 48)
        elif ord(l)<91:
            out[i] = chr((ord(l)- 65 + N) % 26 + 65)
        else:
            out[i] = chr((ord(l)- 97 + N) % 26 + 97)

print(''.join(out))
